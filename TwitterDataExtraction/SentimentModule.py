from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


class SentimentModule:
    @staticmethod
    def sentimentProbability(tweetsByProvince):
        """
        analyse the tweet, then set the positive and negative probability of this tweet
        """
        print("start analysis_____________")
        for province in tweetsByProvince:
            for tweet in province.tweets:
                # text_tb = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
                text_tb = TextBlob(tweet.text)
                # print("positive------- = {}".format(text_tb.sentiment.p_pos))
                print("positive------- = {}".format(text_tb.sentiment.polarity))

                tweet.positivePercentage = text_tb.sentiment.polarity
                tweet.negativePercentage = text_tb.sentiment.subjectivity
        print("end analysis_____________")

        return tweetsByProvince

