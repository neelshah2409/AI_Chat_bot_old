import pandas as pd
import os
import docx

def csvData(data):
    df = pd.read_csv(os.getcwd()+data, skiprows=1, names=["questions", "answers"], encoding='utf-8')
    df.dropna(inplace=True)
    csvdata={}
    csvdata["questions"] = list(df["questions"])
    csvdata["answers"] = list(df["answers"])
    return csvdata

def txtData(data):
    with open(os.getcwd()+data, "r", encoding="utf8") as f:
        question = True
        questions = []
        answers = []
        for i in f.read().split("\n\n"):
            if question:
                questions.append(i)
                question = not question
            else:
                answers.append(i)
                question = not question
        txtdata = {}
        txtdata["questions"] = questions
        txtdata["answers"] = answers
        return txtdata


def docxData(data):
    doc = docx.Document(os.getcwd()+data)
    question = True
    questions = []
    answers = []
    for i in list(doc.paragraphs)[0].text.split("\n\n"):
        if question:
            questions.append(i)
            question = not question
        else:
            answers.append(i)
            question = not question
    docxdata = {}
    docxdata["questions"] = questions
    docxdata["answers"] = answers
    return docxdata

