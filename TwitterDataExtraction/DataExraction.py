import tweepy

consumer_key = 'gfWzybYMttpOTZPd3YgglEDtT'
consumer_secret = 'HkIvtabkS3k9ueswwmdTXjB24DqQz8r0iBXzK1sj9xSvTVunBq'
access_token = '1192624255130845184-47D3JNJDALjEFFuQKbt3CDusV8jNxV'
access_token_secret = 'piYcEkJqVj6wDxxJVrJcv01UhFLfXif22TClZWdx6T8nU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

provinceLatitudes = ["","",]
provinceLongtitudes = []
provinceRadius = []

tweetsByProvince = [];

tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,geocode='',
                           lang="en",
                           since="2019-01-01").items()


tweepy.api.search
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
