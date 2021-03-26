import requests
# Importing requests 

url = "https://api.tellonym.me/accounts/forgotpassword"
# Check Email Linked API URL

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Accept-Language": "en",
	} 
# Check Email Linked API Headers

email = input("Email: ") 
# Email Input

data = {
	"email": email,
	"limit": 16
}
# Check Email Linked API Data

req = requests.post(url, json=data, headers=headers)
# Check Email Linked API Request
if req.status_code == 200:
	print("Linked Email !")
	# Linked Email

elif "PARAMETER_MISSING" in req.text:
	print("Missing Something, Try Again")
	# Missing Data

elif "The entry you were looking for could not be found." in req.text:
	print("Not Linked Email !")
	# Not Linked

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
