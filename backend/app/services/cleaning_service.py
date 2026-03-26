import pandas as pd

def clean_dataset(path):

    df=pd.read_csv(path)

    df=df.drop_duplicates()

    df=df.fillna(

    df.mean(

    numeric_only=True

    )

    )

    df.to_csv(path,index=False)

    return {

        "rows":len(df)

    }