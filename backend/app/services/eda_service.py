import pandas as pd

def analyze(path):

    df=pd.read_csv(path)

    return {

        "shape":df.shape,

        "columns":

        df.columns.tolist(),

        "missing":

        df.isnull().sum().to_dict(),

        "describe":

        df.describe().to_dict()

    }