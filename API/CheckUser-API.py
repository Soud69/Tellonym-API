import requests
# Importing requests 

username = input("Username: ")
# Username Input

url = f"https://api.tellonym.me/accounts/check?username={username}&limit=13"
# Check API URL


headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Accept-Language": "en",
	} 
# Check API Headers

req = requests.get(url, headers=headers)
# Check API Request

if "USERNAME_ALREADY_IN_USE" in req.text:
	print("Username Taken, Try Again")
	# Taken Username

elif 'username":true' in req.text:
	print("Username Available")
	# Found Username

elif "PARAMETER_INVALID" in req.text:
	print("Invalid Username")
	# Username Error/Not Supported

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
