import json
from json import JSONEncoder

from Tweet import Tweet


class TweetsByProvince:
    name = ""
    tweets = [Tweet(None, None, None, None, None)]

    def __init__(self, name, tweets):
        self.name = name
        self.tweets = tweets


class TweetsByProvinceEncoder(JSONEncoder):
    def default(self, o):
        tmp = {}
        if isinstance(o, TweetsByProvince):
            for tweet in o.tweets:
                tmp.update(tweet.__dict__)
            return tmp
        else:
            return json.JSONEncoder.default(self, o)
