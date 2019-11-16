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

            positivePercentageSum = 0.0
            negativePercentageSum = 0.0
            for tweet in province.tweets:
                # text_tb = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
                text_tb = TextBlob(tweet.text)
                # print("positive------- = {}".format(text_tb.sentiment.p_pos))
                print("positive------- = {}".format(text_tb.sentiment.polarity))

                tweet.positivePercentage = text_tb.sentiment.polarity
                tweet.negativePercentage = text_tb.sentiment.subjectivity
                positivePercentageSum += tweet.positivePercentage
                negativePercentageSum += tweet.negativePercentage
            province.averageNegativePercentage = negativePercentageSum / province.tweets.count
            province.averagePositivePercentage = positivePercentageSum / province.tweets.count
        print("end analysis_____________")

        return tweetsByProvince

