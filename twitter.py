#import requests
import pandas as pd
import tweepy
client = tweepy.Client('AAAAAAAAAAAAAAAAAAAAACK8dgEAAAAAKPrElap%2BuwrTifb2d3t%2FMvab0jc%3DWXhCbe542Qxo3ci6Itl2OUMmj0zuVkzDCgTA6c2C3QlfpVz3hF')

#tw_df = str(client.get_users_tweets(44196397, end_time=None, exclude=None, expansions=None, max_results=100, media_fields=None, pagination_token=None, place_fields=None, poll_fields=None, since_id=None, start_time=None, tweet_fields=None, until_id=None, user_fields=None, user_auth=False))

def write(id):
    tw_df = str(client.get_users_tweets(id, end_time=None, exclude=None, expansions=None, max_results=100, media_fields=None, pagination_token=None, place_fields=None, poll_fields=None, since_id=None, start_time=None, tweet_fields=None, until_id=None, user_fields=None, user_auth=False))
    f = open('user_tweets.csv', "w", encoding="utf-8")
    f.write(tw_df)
    f.close()
    tweets = pd.read_csv('user_tweets.csv')


f = open('user_tweets.csv', "w", encoding="utf-8")
f.write(tw_df)
f.close()
tweets = pd.read_csv('user_tweets.csv')

def return_twitterid(screen_name):
    twitterid = client.get_user(username=screen_name)
    #print(type(twitterid)) 
    return (f"{twitterid.data.id}")