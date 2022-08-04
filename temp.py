# # # import docx
# # #
# # # doc = docx.Document("/Users/harshilkhamar/Desktop/temp.docx")
# # # print(list(doc.paragraphs)[0].text.split("\n\n"))
# # # # for i in f.read().split("\n\n"):
# # # #     print(question)
# # # #     if question:
# # # #         questions.append(i.encode("utf8", errors="replace"))
# # # #         question = not question
# # # #     else:
# # # #         answers.append(i.encode("utf8", errors="replace"))
# # # #         question = not question
# # # #
# # # # if(len(questions) == len(answers)):
# # # #     print(questions,answers)
# # # # else:
# # # #     pass
# # #
# # #
# # #
# #
# # from rest_framework_api_key.crypto import KeyGenerator
# # print(KeyGenerator.generate())
#
# from googletrans import Translator,LANGUAGES
#
# translator = Translator(service_urls=['translate.googleapis.com'])
# print(translator.translate("majama",src="gu",dest="en").text)

from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()

parser.parse(text)
# print(parser.parse(text)['result'])