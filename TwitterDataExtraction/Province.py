class Province:
    centerLongtitude = ""
    centerLatitude = ""
    name = ""
    radius = ""
    geoCode = ""

    def __init__(self, longtitude, latitude, name, radius):
        self.centerLatitude = latitude
        self.centerLongtitude = longtitude
        self.name = name
        self.radius = radius
        self.geoCode = self.centerLatitude + "," + self.centerLongtitude + "," + radius

