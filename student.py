import numpy as np
import pandas as pd
import joblib
from flask import Flask,request,jsonify

model = joblib.load("student_model.pkl")

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def start():
  return "welcome"

@app.route("/check",methods = ["POST"])
def predictions():
  try:
   data = request.get_json()

   main_data = pd.DataFrame([data],columns = ["hours_studied","sleep_hours","attendance"])

   prediction = model.predict(main_data)

   results = np.array(prediction).tolist()

   return jsonify(results[0])
  
  except Exception as e:
    return jsonify (e)
  

if __name__=="__main__":
  app.run(debug=True)




