import tweepy
from time import sleep

# Import Twitter credentials from credentials.py
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file=open('sample.txt','r')
file_lines=my_file.readlines()
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
# Add try ... except block to catch and output errors
    try:
        print(line)
        # Add if statement to ensure that blank lines are skipped
        if line != '\n':
            api.update_status(line)

        # Add an else statement with pass to conclude the conditional statement
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(10)
