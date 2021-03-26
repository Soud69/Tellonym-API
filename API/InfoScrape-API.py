import requests
import json
# Importing Json And requests 

# Note: We Need Auth Token Fron Login-API.py
# token = json.loads(req.text)["accessToken"]

url = "https://api.tellonym.me/accounts/myself?adExpId=80&limit=16"
# Scrape API URL

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
# Scrape API Headers

req = requests.get(url, headers=headers)
# Scrape API Request

scrape = json.loads(req.text)
# Parsing Json Data

user_id = scrape["id"]
email = scrape["email"]
display_name = scrape["displayName"]
username = scrape["username"]
account_type = scrape["type"]
account_lang = scrape["lang"]
account_location = scrape["location"]
twitter_username = scrape["twitterUsername"]
instagram_username = scrape["instagramUsername"]
account_creat = scrape["createdAt"]
account_bio = scrape["aboutMe"]
account_avatar = scrape["avatarFileName"]
account_avatar_url = "https://userimg.tellonym.me/xs/"+account_avatar
account_searchable = scrape["isSearchable"]
account_lastactiveat = scrape["lastActiveAt"]
account_likes = scrape["likesCount"]
account_followers = scrape["followerCount"]
account_anonfollowers = scrape["anonymousFollowerCount"]
account_following = scrape["followingCount"]
account_tell = scrape["tellCount"]
account_answer = scrape["answerCount"]
account_verified = scrape["isVerified"]
# Account Info Scrape

print(f"""
ID: {user_id}
Email: {email} 
Name: {display_name}
Username: {username}
Type: {account_type}
Language: {account_lang}
Location: {account_location}
Twitter: {twitter_username}
Instagram: {instagram_username}
Created At: {account_creat}
Bio: {account_bio}
Avatar: {account_avatar}
Avatar URL: {account_avatar_url}
Searchable: {account_searchable}
Last Active At: {account_lastactiveat}
Likes: {account_likes}
Followers: {account_followers}
Anon Followers: {account_anonfollowers}
Following: {account_following}
Tell: {account_tell}
Answers: {account_answer}
Verified: {account_verified}
""")
# print Account Info
