import os, tweepy

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY = os.environ['TWITTER_ACCESS_KEY']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

class twitter(object):
    @staticmethod
    def send(tweet):
        if (len(tweet) > 140):
            return print('Tweet body is more than 140 characters, please shorten')
        return api.update_status(tweet)
