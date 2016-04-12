from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import tweepy

import json

#User credentials from your twitter app 
access_token = "INSET_ACCESS_TOKEN_HERE"
access_token_secret = "INSERT_TOKEN_SECRET_HERE"
consumer_key = "INSERT_CONSUMER_KEY_HERE"
consumer_secret = "INSERT_CONSUMER_SECRET_HERE"

woeid=2391585 #woeid for san francisco

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
sf_trends = api.trends_place(woeid)
data = sf_trends[0]
trends = data['trends']
names = [trend['name'] for trend in trends]

namesJoined = '\n'.join(names)

print(namesJoined)

#To get a list of available woeid's use the code below
#trends_available = api.trends_available()
#print(json.dumps(trends_available, indent=4))
