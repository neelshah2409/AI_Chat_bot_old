import pandas as pd
import os

def csvData(data):
    df = pd.read_csv(os.getcwd()+data, skiprows=1, names=["questions", "answers"])
    csvdata = { "questions": [df["questions"][i] for i in range(df.shape[0])], "answers": [df["answers"][i] for i in range(df.shape[0])] }
    return csvdata
