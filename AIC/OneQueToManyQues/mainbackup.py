import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import json
intentsfile = json.loads(open('intents.json').read())





# def set_seed(seed):
#   torch.manual_seed(seed)
#   if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(seed)
#
# set_seed(42)
#
# model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_paraphraser')
# tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_paraphraser')
#
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print ("device ",device)
# model = model.to(device)
# print("Question Please?")
# sentence = str(input())
# print(sentence)
# # sentence = "What are the ingredients required to bake a perfect cake?"
# # sentence = "What is the best possible approach to learn aeronautical engineering?"
# # sentence = "Do apples taste better than oranges in general?"
#
#
# text =  "paraphrase: " + sentence + " </s>"
#
#
# max_len = 256
#
# encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
# input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)
#
#
# # set top_k = 50 and set top_p = 0.95 and num_return_sequences = 3
# beam_outputs = model.generate(
#     input_ids=input_ids, attention_mask=attention_masks,
#     do_sample=True,
#     max_length=256,
#     top_k=120,
#     top_p=0.98,
#     early_stopping=True,
#     num_return_sequences=10
# )
#
#
# print ("\nOriginal Question ::")
# print (sentence)
# print ("\n")
# print ("Paraphrased Questions :: ")
# final_outputs =[]
# for beam_output in beam_outputs:
#     sent = tokenizer.decode(beam_output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
#     if sent.lower() != sentence.lower() and sent not in final_outputs:
#         final_outputs.append(sent)
# ques = []
# for i, final_output in enumerate(final_outputs):
#     ques.append(final_output)
#
#     print("{}: {}".format(i, final_output))

# dict = {
#    "tag": "queone\n" ,
#     "patterns": ques + '\n',
#     "responses": ""
#   },


def updatePatterns(input):
    def set_seed(seed):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    set_seed(42)

    model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_paraphraser')
    tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_paraphraser')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # print("device ", device)
    model = model.to(device)
    # print("Question Please?")
    sentence = str(input)
    # print(sentence)
    # sentence = "What are the ingredients required to bake a perfect cake?"
    # sentence = "What is the best possible approach to learn aeronautical engineering?"
    # sentence = "Do apples taste better than oranges in general?"

    text = "paraphrase: " + sentence + " </s>"

    max_len = 256

    encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    # set top_k = 50 and set top_p = 0.95 and num_return_sequences = 3
    beam_outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        do_sample=True,
        max_length=256,
        top_k=120,
        top_p=0.98,
        early_stopping=True,
        num_return_sequences=10
    )

    # print("\nOriginal Question ::")
    # print(sentence)
    # print("\n")
    # print("Paraphrased Questions :: ")
    final_outputs = []
    for beam_output in beam_outputs:
        sent = tokenizer.decode(beam_output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        if sent.lower() != sentence.lower() and sent not in final_outputs:
            final_outputs.append(sent)
    ques = []
    for i, final_output in enumerate(final_outputs):
        ques.append(final_output)

        # print("{}: {}".format(i, final_output))
    return ques
# list = [1,2,3,4,5,6]

def updatejson(intent):

    a_file = open("intents.json", "a")
    json.dump(intent ,a_file)
    a_file.write(',')
    a_file.close()


for intent in intentsfile['intents']:
    ques = updatePatterns(intent.get('patterns')[0])
    for i in ques:
        print(i)
        intent.get('patterns').append(i)

    print(intent.get('patterns'))
    updatejson(intent)

    print('done')







