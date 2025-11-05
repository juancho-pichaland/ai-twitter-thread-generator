import pandas as pd

def read_topics(path="data/topics.csv"):
    df = pd.read_csv(path)
    return df["topic"].tolist()
