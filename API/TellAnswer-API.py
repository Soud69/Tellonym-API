import requests
# Importing requests 

# Note: We Need Auth Token Fron Login-API.py
# token = json.loads(req.text)["accessToken"]

url = "https://api.tellonym.me/answers/create"
# Answer API URL

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
# Answer API Headers

user_id = input("Tell ID: ")
# Tell_ID Input

message = input("Reply: ")
# Reply Input

data = {
	"limit": 16,
	"answer": message,
	"tellId": user_id
}
# Answer API Data

req = requests.post(url, json=data, headers=headers)
# Answer API Request

if "TELL_TOO_SHORT" in req.text:
	print("Tell Is Too Short, Try Again")
	# Short Tell

elif req.status_code == 200:
	print("Sent Success")
	# Sent Answer

elif "The entry you were looking for could not be found." in req.text:
	print("Tell ID Not Found")
	# User ID Wrong

elif "PARAMETER_MISSING" in req.text:
	print("Missing Input")
	# Missing Input

elif "PARAMETER_INVALID" in req.text:
	print("Invalid Input")
	# Wrong Input
	
else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
