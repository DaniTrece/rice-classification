import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = "model_C=0.5.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

app = Flask("rice_classification")


@app.route("/predict", methods=["POST"])
def predict():
    rice_features = request.get_json()

    print(rice_features)
    y_pred = model.predict_proba(rice_features)[0, 1]
    print(y_pred, y_pred >= 0.5)

    # y_pred < 0.5 -> Cammeo
    # y_pred >= 0.5 -> Osmancik
    rice = ["Cammeo", "Osmancik"][int(y_pred >= 0.5)]

    result = {"rice_variety": rice}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
