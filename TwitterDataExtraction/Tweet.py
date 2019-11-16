class Tweet:
    longtitude = ""
    latitue = ""
    positivePercentage = 0.0
    negativePercentage = 0.0
    name = ""
    text = ""

    def __init__(self, longtitude, latitude, name, text, positivePercentage=0.0, negativePercentage=0.0):
        self.latitue = latitude
        self.longtitude = longtitude
        self.name = name
        self.text = text
