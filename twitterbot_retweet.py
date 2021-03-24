import tweepy
import datetime
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets,like tweets and follow users") your text
print("Bot Settings") your text 
print("Like Tweets :", LIKE) # your text
print("Follow users :", FOLLOW) # your text

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet') your text

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet') your text

        # Follow the user who tweeted
        #check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        sleep(SLEEP_TIME)

# create def Bye():        
def Bye():
    print('Bye!') your text
    
Bye() Close

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
