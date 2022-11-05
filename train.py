import pandas as pd


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from tqdm.auto import tqdm

import pickle


df = pd.read_csv("Rice_Cammeo_Osmancik.csv", sep=";", decimal=",")
df.columns = df.columns.str.lower().str.replace(" ", "_")

seed = 13
test_size = 0.25
n_kfolds = 4
max_iter = 1000

kfold = KFold(n_splits=n_kfolds, shuffle=True, random_state=seed)

df["class"] = df["class"].map(dict(Cammeo=0, Osmancik=1))

df_full_train, df_test = train_test_split(df, test_size=0.25, random_state=seed)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_test = df_test["class"].values

del df_test["class"]


def train(X_train, y_train, C=1.0):
    model = LogisticRegression(C=C, max_iter=max_iter)
    model.fit(X_train, y_train)
    return model


def predict(df, model):
    y_pred = model.predict_proba(df)[:, 1]
    return y_pred


models = []
scores = []
idx = 0
C = 0.5
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train["class"].values
    y_val = df_val["class"].values

    del df_train["class"]
    del df_val["class"]

    model = train(df_train.values, y_train, C=C)
    y_pred = predict(df_val.values, model)

    auc = roc_auc_score(y_val, y_pred)

    scores.append((idx, auc))
    models.append(model)
    idx += 1

scores_sorted = sorted(scores, key=lambda s: s[1], reverse=True)

logistic_regression_model = models[scores_sorted[0][0]]

output_file = f"model_C={C}.bin"

with open(output_file, "wb") as f_out:
    pickle.dump(model, f_out)

print(f"the model is saved to {output_file}")
