from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy

consumer_key = "9Q5Y9X28oKCiSFHR7iDe28f2h"
consumer_secret = "SD269dnDY3lO8aYsmGKtV5kpEN3UcvvDNp9WXHVkfaj9vwRDlr"
access_token = "833052473266991104-yOy0yfffXCpy1oUNXmgdv4HaBiFidbM"
access_token_secret = "mVE9Vfl3QF1GqZbzSwBPVLyapwc4ieKSpcpVS60IvdLpn"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

print (auth_api)
item = auth_api.get_user("blizzard01604")
print("name: " + item.name)
print("screen_name: " + item.screen_name)
print("description: " + item.description)
print("statuses_count: " + str(item.statuses_count))
print("friends_count: " + str(item.friends_count))
print("followers_count: " + str(item.followers_count))

item = auth_api.user_timeline ("blizzard01604")


def searchTweets () :
    # empty list to store parsed tweets
    tweets = []
    # call twitter api to fetch tweets
    q = ""
    a = str(q + " $EDIT")
    b = str(q + " $TSLA")
    c = str(q + " $AMZN")
    #fetched_tweets = auth_api.search(a, count=2000, tweet_mode="extended")
    # parsing tweets one by one
    tweets = tweepy.Cursor(auth_api.search, "$EDIT", tweet_mode="extended").items(1000)

    for tweet in tweets:
        info = tweet.user.name + "(" + str(tweet.user.followers_count) + ") [" + tweet.created_at.strftime("%m-%d-%H-%M") + "] " + tweet.full_text
        print (info)
    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets

searchTweets()
