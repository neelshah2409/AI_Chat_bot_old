import docx

doc = docx.Document("/Users/harshilkhamar/Desktop/temp.docx")
print(list(doc.paragraphs)[0].text.split("\n\n"))
# for i in f.read().split("\n\n"):
#     print(question)
#     if question:
#         questions.append(i.encode("utf8", errors="replace"))
#         question = not question
#     else:
#         answers.append(i.encode("utf8", errors="replace"))
#         question = not question
#
# if(len(questions) == len(answers)):
#     print(questions,answers)
# else:
#     pass



