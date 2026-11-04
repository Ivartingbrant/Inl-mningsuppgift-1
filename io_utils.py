import pandas as pd

def load_data(data):
    """Läser in csv filen med data och returnerar dataframe"""
    return pd.read_csv(data)


