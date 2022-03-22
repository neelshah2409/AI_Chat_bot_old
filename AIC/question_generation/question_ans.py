# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
# import re
#
# model_name = "deepset/roberta-base-squad2"
# que = ['What should be considered as responses to several distinct pressures?',
#        'What is the main cause of privatisation?',
#        'What does privatisation provide?']
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# ansList = []
# text = '''Policies of privatisation should be considered as responses to several distinct pressures. First,
#      privatisation is a response by the state to internal forces such as increasing fiscal problems (O’Connor, 1973).
#      It provides a means of lessening the state’s fiscal responsibilities by encouraging the development of private alternatives
#       which, theoretically at least'''
#
# for i in que:
#     QA_input = {
#         'question': i,
#         'context': text
#     }
#
#     ansList.append(nlp(QA_input))
#
# full_answer_list = []
# for i in range(len(que)):
#     full_answer_list.append(re.findall(r"([^.]{}[^.])".format(text[ansList[i]["start"]:ansList[i]["end"]]), text))
#
# # print(ansList)
# # print(full_answer_list)
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
