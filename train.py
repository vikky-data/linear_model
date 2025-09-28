import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify


model = joblib.load("vikky_first_model.pkl")
app = Flask(__name__)

@app.route("/vikky", methods= ["GET"])

def test_server():
  return "vikky is building her first API"


@app.route("/predict", methods =["POST"])

def get_predictions():
  try:
    data = request.get_json()

    real_data = pd.DataFrame([data], columns=["Avg. Session Length","Time on App","Time on Website","Length of Membership"])
    predictions = model.predict(real_data)
    result = np.array(predictions).tolist()

    return jsonify({"predictions": result[0]})
  except Exception as e:
    return jsonify(e)

if __name__ == "__main__":
  app.run(debug=True)