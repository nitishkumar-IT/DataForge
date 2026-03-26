import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

import joblib

def train(path,target):

    df=pd.read_csv(path)

    X=df.drop(target,axis=1)

    y=df[target]

    X_train,X_test,y_train,y_test=train_test_split(

    X,

    y,

    test_size=0.2

    )

    model=RandomForestRegressor()

    model.fit(

    X_train,

    y_train

    )

    accuracy=model.score(

    X_test,

    y_test

    )

    joblib.dump(

    model,

    "models/model.pkl"

    )

    return {

        "accuracy":accuracy

    }