import requests 

url = "http://127.0.0.1:5000/check"

data = {
  	"hours_studied":7,	
    "sleep_hours":5	,
    "attendance":80

}

response = requests.post(url,json= data)

print(response.status_code)
print(response.text)