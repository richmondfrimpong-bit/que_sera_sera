import tweepy
import keys
import pandas as pd

auth = tweepy.OAuthHandler(keys.API_key, keys.API_key_secret,
                           keys.Access_token, keys.Access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

nasa = api.me()

#search_query = " 'Elon Musk' 'fired' -filter:retweets AND -filter:replies AND -filter:links "
#no_of_tweets = 100

#try:
#    tweets = api.search_tweets(q= search_query,lang='en',count=no_of_tweets, tweet_mode='extended')
#    attributes_container = [[tweet.user.name, tweet.created_at,tweet.favorit_count,tweet.source,tweet.full_text] for tweet in tweets]
#    columns =['Username', 'Location', 'No. of likes', 'Source', 'tweet']

#    tweet_df = pd.DataFrame(attributes_container,columns=columns)
#except BaseException as e:
#    print('Status failed on:',str(e))
