#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#User Credentials from twitter app 
access_token = "INSET_ACCESS_TOKEN_HERE"
access_token_secret = "INSERT_TOKEN_SECRET_HERE"
consumer_key = "INSERT_CONSUMER_KEY_HERE"
consumer_secret = "INSERT_CONSUMER_SECRET_HERE"

word1='google'

word2='tesla'

#StdOutListener derived from StreamListener. Prints tweets.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #Twitter authetification to connection to Twitter Streaming API
    listen = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listen)

    #Filter tweets using keywords
    stream.filter(track=[word1,word2])
