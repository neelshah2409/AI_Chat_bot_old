import random
import json
import pickle
import numpy as np
import nltk
# from tensorflow import keras
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.optimizers import SGD
from keras.optimizers import gradient_descent_v2
import os


ACCURACY_THRESHOLD = 0.95

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > ACCURACY_THRESHOLD):
            print("\nReached %2.2f%% accuracy, so stopping training!!" %(ACCURACY_THRESHOLD*100))
            self.model.stop_training = True

callbacks = myCallback()

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from tensorflow import keras


def trainTheChatBot(id):
    lemmatizer = WordNetLemmatizer()
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",encoding='utf-8').read())


    words = []
    classes = []
    documents = []
    ignore_letters = {'?', '!', '.', ','}

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
    words = sorted(set(words))

    classes = sorted(set(classes))

    pickle.dump(words, open(f"{os.getcwd()}{os.sep}Training{os.sep}words{os.sep}words{id}.pkl", 'wb'))
    pickle.dump(classes, open(f"{os.getcwd()}{os.sep}Training{os.sep}classes{os.sep}classes{id}.pkl", 'wb'))

    training = []
    output_empty = [0] * len(classes)

    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    model = Sequential()
    model.add(Dense(512, input_shape=(len(train_x[0]),), activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(len(train_y[0]), activation='softmax'))
    # sgd = gradient_descent_v2.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    # tf.keras.optimizers.Adam(
    #     learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=False,
    #     name='Adam', **kwargs
    # )

    optimizer = keras.optimizers.Adam(lr=0.003, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    # model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=optimizer, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=2000, verbose=1, callbacks=[callbacks])
    curr = os.getcwd()
    model.save(f"{os.getcwd()}{os.sep}Training{os.sep}modelData{os.sep}chatbotmodel{id}.h5", hist)
    print("Sucess File Updated")

if __name__ == '__main__':
    trainTheChatBot()

