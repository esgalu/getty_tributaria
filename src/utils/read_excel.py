import pandas as pd


def read_file(path):
    df = pd.read_excel(path)
    df = df.replace({'In/Out': {'In': 1, 'Out': 0}})

    return df

