#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#User Credentials from twitter app 
access_token = "714148187087511552-NQLJ69wMV4G32zCoIjMdPdOsbc71lGA"
access_token_secret = "joGlBVfELJkPyIObQCabRVdIy8lT3gXpATLz9xplN1sBI"
consumer_key = "oAUT454OIA9BbJcESTJkcaAa6"
consumer_secret = "SOlauJ7HdIqwA57BDtZV6W1BCsWjulaihfcVU0aiyW2yiXHdc4"

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
