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
                print("polarity------- = {}".format(text_tb.sentiment.polarity))

                # use sentiment.polarity to classify polarity
                if text_tb.sentiment.polarity >= 0:
                    tweet.positivePercentage = text_tb.sentiment.polarity * 0.5 + 0.5
                    tweet.negativePercentage = 1 - tweet.positivePercentage
                else:
                    tweet.negativePercentage = -0.5 * text_tb.sentiment.polarity + 0.5
                    tweet.positivePercentage = 1 - tweet.negativePercentage

                # tweet.positivePercentage = text_tb.sentiment.polarity * flag
                # tweet.negativePercentage = 1 - abs(tweet.positivePercentage)
                positivePercentageSum += tweet.positivePercentage
                negativePercentageSum += tweet.negativePercentage
            province.averageNegativePercentage = negativePercentageSum / len(province.tweets)
            province.averagePositivePercentage = positivePercentageSum / len(province.tweets)
        print("end analysis_____________")

        return tweetsByProvince


if __name__ == '__main__':
    # test case for sentiment polarity
    texts = [
        "The internet in Iran is effectively shut down, which has made it difficult to get a clear picture of " \
        "what's happening in the country. DW verified videos from inside the country and summarized events over " \
        "the last week. ",
        "“How do I look loud,” B shouts at the camera in response. “How do I look loud? I’m loud? I don’t even think "
        "I’m like loud. Suck my ass.” ",
        "Beijing is signaling a much tougher line on Hong Kong, striking at the heart of one country, two systems.",
        "Very disappointed! When I wear them for the first time I felt them weird like a air bubble inside the sole ! "
        "After 3months I have a hole inside the sole of the shoes and it very inconfortable",
        "These pair of shoes are the worst i’ve Ever got. They’re not comfy and the lining of the shoes falls apart "
        "and it makes a very bad odour . I love Clark’s shoes but this is such a bad experience ! ",
    ]
    for text in texts:
        tb_data = TextBlob(text)
        positive = negative = None

        # solution1
        # if tb_data.polarity >= 0:
        #     positive = tb_data.polarity
        #     negative = 1 - positive
        # else:
        #     negative = -1 * tb_data.polarity
        #     positive = 1 - negative

        # solution2
        if tb_data.polarity >= 0:
            positive = tb_data.polarity * 0.5 + 0.5
            negative = 1 - positive
        elif tb_data.polarity < 0:
            negative = tb_data.polarity * -0.5 + 0.5
            positive = 1 - negative

        print("\n{} \nPolarity: {}".format(text, tb_data.polarity))
        print("Positive: {:.5f}\nNegative: {:.5f}\n\n".format(positive, negative))
