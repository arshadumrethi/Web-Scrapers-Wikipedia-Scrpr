import tweepy
from textblob import TextBlob

#Getting Twitter Api access.
consumer_key = 'RkWUk9KAWQshjDRHPGgSh8JP4'
consumer_secret = '37ZPIYgMkB0eTlT3kqUaKdiOgEYu3ZZNuJE4KY9pu0LZ4bpnb9'

access_token = '236304102-URrGDhfhebG7qwzTzV0ie6qge8JJHNYmQaoxREFM'
access_token_secret = 'ZYc85aQkLcpaQcZCceIzgPpsQDeZetXdi8ozRgJ4QW0vs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Setting the topic that the api will scrape.
public_tweets = api.search('Trump')

#Printing tweet and its corresponding sentiment value.
for tweet in public_tweets:
    print analysis = TextBlob(tweet.text)
    print senti = analysis.sentiment
