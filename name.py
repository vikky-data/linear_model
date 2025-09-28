import requests

url = "http://127.0.0.1:5000/predict"

data = {
   "Avg. Session Length": "23",
   "Time on App": 21,
   "Time on Website": 12,
   "Length of Membership": 32

}
 

response = requests.post(url, json=data)

print("status code:", response.status_code)

print("predictions:" , response.text)


