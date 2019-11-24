import config
import tweepy
import random
import subprocess as s

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token 
access_token_secret = config.access_token_secret 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='GreatestQuotes', count=500)
tweet = random.choice(tweets).text.split(' - ')
message = tweet[0]
title = tweet[1]


def sendmessage():
    s.call(['notify-send', title, message])

sendmessage()
