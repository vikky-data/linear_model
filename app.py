import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify

model = joblib.load("usa_housing_model.pkl")

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def begin():
  return "welcome to this page"

@app.route("/predict",methods  = ["POST"])
def predictions():
  try:
    data = request.get_json()

    main_data = pd.DataFrame([data],columns = ["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms","Area Population"])
    predict = model.predict(main_data)
    result = np.array(predict).tolist()

    return jsonify(result[0])
  
  except Exception as e:
    return jsonify(e)
  

if __name__ == "__main__":
  app.run(debug=True)