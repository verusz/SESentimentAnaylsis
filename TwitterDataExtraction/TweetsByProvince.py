import json
import time
from json import JSONEncoder

from Tweet import Tweet


class TweetsByProvince:
    name = ""

    longitude = ""
    latitude = ""
    averagePositivePercentage = 0.0
    averageNegativePercentage = 0.0
    tweets = [Tweet(None, None, None, None, None)]

    def __init__(self, name, tweets, longitude, latitude):
        self.name = name
        self.tweets = tweets
        self.longitude = longitude
        self.latitude = latitude


class TweetsByProvinceEncoder(JSONEncoder):
    def default(self, o):
        outer_TweetsByProvince = {}
        if isinstance(o, TweetsByProvince):
            inner_tweet = []
            for tweet in o.tweets:  # fetch the tweets' attribute of an instance of TweetsByProvince
                # print(tweet.__dict__)
                inner_tweet.append(tweet.__dict__)
                # print(inner_tweet)
            outer_TweetsByProvince['name'] = o.name
            outer_TweetsByProvince['longitude'] = o.longitude
            outer_TweetsByProvince['latitude'] = o.latitude
            outer_TweetsByProvince['averageNegativePercentage'] = o.averageNegativePercentage
            outer_TweetsByProvince['averagePositivePercentage'] = o.averagePositivePercentage
            outer_TweetsByProvince['tweets'] = inner_tweet
            print(outer_TweetsByProvince)
            return outer_TweetsByProvince
        else:
            return json.JSONEncoder.default(self, o)
