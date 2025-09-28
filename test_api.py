import requests

url = "http://127.0.0.1:5000/predict"

data = {
  "Avg. Area Income":79545,
  "Avg. Area House Age" :5,
  "Avg. Area Number of Rooms" :7,
  "Avg. Area Number of Bedrooms":4,
  "Area Population":23086


}

response = requests.post(url, json=data)

print("status code:", response.status_code)

print("predictions:" , response.text)
