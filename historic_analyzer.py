import tweepy
from textblob import TextBlob
import nltk
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

# consumer_key = 'ykU3M4ySMu5awQHcU2b1Td0uS'
# consumer_secret = '9xkTXsldiSiQ38O4BO2feaLfparq7ZTmKUTmi2Ftx14V18Je0W'
# access_token = '924306929660207104-FFGM4PyjGjKWd80PrHHxt5d2dObXemA'
# access_token_secret = 'ezvyStkTjLP1MgcEeknmoPb8aJSidO8UK6mZCxoErmlsW'

print(sys.argv)
consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('sys.argv[5]', count=100)
psenti = []
nsenti = []
zsenti = []
for tweet in public_tweets:
    analysis = TextBlob(tweet.text.strip())
    senti = analysis.sentiment.polarity
    if senti > 0:
        psenti.append(senti)
    elif senti < 0:
        nsenti.append(senti)
    else:
        zsenti.append(senti)
sns.set_style('darkgrid')
plt.figure(figsize= (20,6))
plt.plot(psenti, 'g+', psenti,'g-' ,label = 'positive polarity')
plt.plot(nsenti, 'ro',nsenti,'r-' ,label = 'negative polarity')
plt.ylabel('<-----------------  Sentiment polarity   ------------------------->')
plt.xlabel('<-----------------  Tweet   ------------------------->')
# plt.plot(zsenti, 'bo', label = 'compound polarity')
plt.legend()
plt.show()
