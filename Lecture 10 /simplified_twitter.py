# Lecture 10 - Feb 6 
# simplified_twitter.py

from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_key

username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_key.CONSUMER_KEY
consumer_secret = secret_key.CONSUMER_SECRET
access_token = secret_key.ACCESS_KEY
access_secret = secret_key.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends

baseurl = "https://api.twitter.com/1.1/statuses/user_timeline.json"
parameter = {}
parameter["screen_name"] = username
parameter["count"] = num_tweets

user_tweets = requests.get(baseurl, params = parameter, auth = auth).text
user_tweets_list = json.loads(user_tweets) # Get a list of user tweets

for tweet in user_tweets_list:
	print(tweet["user"]["name"], ":") 
	print(tweet['text'])
	print("--------------")
