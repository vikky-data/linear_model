import numpy as np 
import pandas as pd
import joblib
from flask import Flask, request, jsonify

model = joblib.load("farm.pkl")
app = Flask(__name__)

@app.route("/test",methods = ["GET"])
def show():
  return "welcome to my page"

@app.route("/predict",methods = ["POST"])
def prediction():
  try:
   data = request.get_json()

   real_data = pd.DataFrame([data],columns = ["Soil_pH	Soil_Moisture","Temperature_C","Rainfall_mm",	"Fertilizer_Usage_kg","Pesticide_Usage_kg",	"Crop_Yield_ton"])

   predict = model.predict(real_data)
   result = np.array(predict).tolist()


   return jsonify(result[0])


  except Exception as e:
    return jsonify(e)



if __name__ == "__main__":
 app.run(debug = True)