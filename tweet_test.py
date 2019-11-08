from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


class Tweet:
    latitude, longitude = None, None
    text = None
    pos_prob, neg_prob = None, None

    def __init__(self, txt, lat=None, long=None):
        """
        initialize the tweet instance with latitude, longitude and text
        :param lat:
        :param long:
        :param txt:
        """
        self.latitude = lat
        self.longitude = long
        self.text = txt
        self.pos_prob = None
        self.neg_prob = None

    def prob(self):
        """
        analyse the tweet, then set the positive and negative probability of this tweet
        """
        text_tb = TextBlob(self.text, analyzer=NaiveBayesAnalyzer())
        self.pos_prob = text_tb.sentiment.p_pos
        self.neg_prob = text_tb.sentiment.p_neg

    def __str__(self):
        return "Tweet: {}\n Location:({}, {})\n Probability of Positive: {}\n Probability of Negative: {}\n".format(
            self.text, self.latitude, self.longitude, self.pos_prob, self.neg_prob)


if __name__ == '__main__':
    text = "U.S. Senator for Kentucky | I fight for the Constitution, individual liberty and the freedoms that make " \
           "this country great. "
    tw_ob = Tweet(txt=text)
    tw_ob.prob()
    print(tw_ob)
