import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import json
import os


intentsfile = json.loads(open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json').read())

model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_paraphraser')
tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_paraphraser')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
print("i am paraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

def write_json(data, filename=f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def updatejson(intent):
    a_file = open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json", "a")
    json.dump(intent ,a_file)
    a_file.write(',')
    a_file.close()

def updatePatterns(input):
    set_seed(42)
    sentence = str(input)
    text = "paraphrase: " + sentence + " </s>"
    max_len = 256
    encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)
    beam_outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        do_sample=True,
        max_length=256,
        top_k=120,
        top_p=0.98,
        early_stopping=True,
        num_return_sequences=10
    )

    final_outputs = []
    for beam_output in beam_outputs:
        sent = tokenizer.decode(beam_output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        if sent.lower() != sentence.lower() and sent not in final_outputs:
            final_outputs.append(sent)
    ques = []
    for i, final_output in enumerate(final_outputs):
        ques.append(final_output)
    return ques

# for intent in intentsfile['intents']:
#     ques = updatePatterns(intent.get('patterns')[0])
#     for i in ques:
#         print(i)
#         intent.get('patterns').append(i)
#     print(intent.get('patterns'))
#     updatejson(intent)
#     print('done')





def run_main():
    print("i m from paraphrasing")
    import torch
    from transformers import T5ForConditionalGeneration, T5Tokenizer
    import json
    intentsfile = json.loads(open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json').read())

    model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_paraphraser')
    tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_paraphraser')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    iterate= 0
    for intent in intentsfile['intents']:
        print(intent)
        print(intent.get('patterns'))
        ques = updatePatterns(intent.get('patterns')[0])

        ques.append(intent.get('patterns')[0])

        answer = intent.get('responses')
        # for i in ques:
        #     print(i)
        #     intent.get('patterns').append(i)
        # print(intent.get('patterns'))
        # updatejson(intent)

        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json') as json_file:
            data = json.load(json_file)
            temp = data["intents"]
            y = {"tag": f"Data-{str(iterate + 1)}", "patterns": ques, "responses": answer}
            temp.append(y)
        iterate += 1
        write_json(data)
        print('done from para')


if __name__ == '__main__':
    run_main()