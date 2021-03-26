import requests
import json
# Importing json And requests 

url = "https://api.tellonym.me/tokens/create"
# Login API URL

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Accept-Language": "en",
	} 
# Login API Headers

email = input("Username/Email: ") 
# Email Or Username Input
password = input("Password: ") 
# Password Input

data = {
	"activeExperimentId": 0,
	"password": password,
	"country": "US",
	"deviceName": "Soud’s iPhone",
	"deviceType": "ios",
	"lang": "en",
	"limit": 16,
	"email": email
}
# Login API Data

req = requests.post(url, json=data, headers=headers)
# Login API Request

if "WRONG_CREDENTIALS" in req.text:
	print("Login Failed, Try Again")
	# Wrong Login Info

elif "PARAMETER_MISSING" in req.text:
	print("Missing Something, Try Again")
	# Missing Data

elif "accessToken" in req.text:
	print("Login Success")
	token = json.loads(req.text)["accessToken"]
	# Login Success And Parse Login Token

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
