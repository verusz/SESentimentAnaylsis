import tweepy

from SentimentModule import SentimentModule
from Tweet import Tweet
from Province import Province
from TweetsByProvince import TweetsByProvince


class DataExtraction:
    @staticmethod
    def anaylsis(keywords):
        return DataExtraction.anaylsisImplementation(keywords)

    @staticmethod
    def anaylsisImplementation(keywords):
        consumer_key = 'gfWzybYMttpOTZPd3YgglEDtT'
        consumer_secret = 'HkIvtabkS3k9ueswwmdTXjB24DqQz8r0iBXzK1sj9xSvTVunBq'
        access_token = '1192624255130845184-47D3JNJDALjEFFuQKbt3CDusV8jNxV'
        access_token_secret = 'piYcEkJqVj6wDxxJVrJcv01UhFLfXif22TClZWdx6T8nU'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        Saskatchewan = Province("-105", "55", "Saskatchewan", "769km")
        Alberta = Province("-116", "54", "Alberta", "813km")
        BritishColumbia = Province("-126.5", "54.15", "BritishColumbia", "961km")
        Nunavut = Province("-105", "55", "Nunavut", "1391km")
        NorthwestTerritories = Province("-105", "55", "NorthwestTerritories", "1087km")
        Yukon = Province("-132.405", "64.83", "Yukon", "688km")
        Ontario = Province("-84.75", "49.21", "Ontario", "1037km")
        Québec = Province("-68.43", "53.79", "Québec", "1241km")
        NewBrunswick = Province("-66.42", "46.34", "NewBrunswick", "270km")
        NovaScotia = Province("-63.00", "45.23", "NovaScotia", "235km")
        NewfoundlandAndLabrador = Province("-60.20", "53.49", "NewfoundlandAndLabrador", "636km")
        Manitoba = Province("-95.49", "54.50", "Manitoba", "804km")
        PrinceEdwardIsland = Province("-63.19", "46.51", "PrinceEdwardIsland", "75km")

        provinces = [Saskatchewan, Alberta, BritishColumbia, Nunavut, NorthwestTerritories, Yukon, Ontario, Québec,
                     NewBrunswick, NovaScotia, NewfoundlandAndLabrador, Manitoba, PrinceEdwardIsland]

        tweetsByProvince = []
        # Saskatchewan              | -109.99 | 48.99 | -101.36 | 60.00  769km
        # Alberta                   | -120.00 | 48.99 | -109.99 | 60.00  813
        # British Columbia          | -139.06 | 48.30 | -114.03 | 60.00  961
        # Nunavut                   | -120.68 | 51.64 |  -61.08 | 83.11  1391
        # Northwest Territories     | -136.44 | 60.00 | -101.98 | 78.76  1087
        # Yukon                     | -141.00 | 60.00 | -123.81 | 69.65  688
        # Ontario                   |  -95.16 | 41.66 |  -74.34 | 56.86  1037
        # Québec                    |  -79.76 | 44.99 |  -57.10 | 62.59  1241
        # New Brunswick             |  -69.06 | 44.60 |  -63.77 | 48.07  270
        # Nova Scotia               |  -66.32 | 43.42 |  -59.68 | 47.03  235
        # Newfoundland and Labrador |  -67.80 | 46.61 |  -52.61 | 60.37  636
        #                           |  -61.50 | 47.18 |  -60.13 | 47.80
        # Manitoba                  | -102.03 | 48.99 |  -88.94 | 60.00  804
        # Prince Edward Island      |  -64.41 | 45.95 |  -61.97 | 47.06  75

        for province in provinces:
            print(province.geoCode)
            tweets = tweepy.Cursor(api.search, q=keywords, geocode=province.geoCode,
                                   lang="en",
                                   result_type="recent"
                                   ).items(5)
            provinceTweets = []
            for tweet in tweets:
                formateTweet = Tweet(province.centerLongtitude, province.centerLatitude, province.name, tweet.text)

                print(tweet.created_at, tweet.text)
                provinceTweets.append(formateTweet)

            tweetsByProvince.append(TweetsByProvince(province.name, provinceTweets))

        return SentimentModule.sentimentProbability(tweetsByProvince)
