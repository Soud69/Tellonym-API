import requests
# Importing requests 

# Note: We Need Auth Token Fron Login-API.py
# token = json.loads(req.text)["accessToken"]

url = "https://api.tellonym.me/accounts/settings"
# Settings API URL

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Authorization": f"Bearer {token}",
	"Accept-Language": "en",
	} 
# Settings API Headers

snapchat = input("SnapChat Username: ")
# Snapchat Input

instagram = input("Instagram Username: ")
# Instagram Input

twitter = input("Twitter Username: ")
# Twitter Input

name = input("Display Name: ")
# Name Input

bio = input("Bio: ")
# Bio Input

username = input("Username: ")
# Username Input

data = {
	"snapchat": snapchat,
	"displayName": name,
	"tintColor": 2,
	"twitter": twitter,
	"aboutMe": bio,
	"limit": 16,
	"username": username,
	"instagram": instagram
}
# Settings API Data

req = requests.post(url, json=data, headers=headers)
# Settings API Request

if "USERNAME_ALREADY_IN_USE" in req.text:
	print("Username Taken, Try Again")
	# Taken Username

elif f'username":"{username}",' in req.text:
	print("Changed Success")
	# Success Changed

elif "PARAMETER_INVALID" in req.text:
	print("Invalid Input")
	# Wrong Input
	
else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
