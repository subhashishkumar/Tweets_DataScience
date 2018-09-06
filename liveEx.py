import tweepy
import matplotlib.pyplot as plt
import time
import json
from textblob import TextBlob
from tweepy.streaming import StreamListener
import re

consumer_key = 'ykU3M4ySMu5awQHcU2b1Td0uS'
consumer_secret = '9xkTXsldiSiQ38O4BO2feaLfparq7ZTmKUTmi2Ftx14V18Je0W'
access_token = '924306929660207104-FFGM4PyjGjKWd80PrHHxt5d2dObXemA'
access_token_secret = 'ezvyStkTjLP1MgcEeknmoPb8aJSidO8UK6mZCxoErmlsW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class listener(StreamListener):
    def on_data(self, data):
        global initime
        t = int(calctime())
        all_data = json.loads(data)
        public_tweets = all_data['text'].encode('utf-8')
        public_tweets = ' '.join(re.findall('[a-zA-Z]+', public_tweets))
        str_tweets = TextBlob(public_tweets.strip())
        global positive
        global negative
        global count
        global compound
        count = count + 1
        senti = 0
        for sen in str_tweets:
            senti = senti + sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive = positive + sen.sentiment.polarity
            else:
                negative = negative + sen.sentiment.polarity

        compound = compound + senti
        print(count)
        print(str_tweets)
        print(senti)
        #         print str(positive)+ ' ' + str(negative) + ' ' + str(compound)

        plt.axis([0, 70, -20, 20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t], [positive], 'go', [t], [negative], 'ro', [t], [compound], 'bo')
        plt.show()
        plt.pause(0.0001)
        if count == 200:
            return False
        else:
            return True

    def on_error(self, status):
        print(status)


twitterStream = tweepy.Stream(auth, listener(1))
twitterStream.filter(track=["katy perry"])