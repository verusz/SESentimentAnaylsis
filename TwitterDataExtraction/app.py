from flask import Flask, request, jsonify
from DataExtraction import DataExtraction
from TweetsByProvince import TweetsByProvinceEncoder
import json

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        keywords = request.args.get("keywords")
        data = DataExtraction.anaylsis(keywords)
        # for model in data:
        json_str = TweetsByProvinceEncoder().encode(data)

        j = json.dumps(json_str)
        # print("return data________ {}".format())

        return j

    return 'Nothing Happened!'


@app.route('/zoom', methods=['GET'])
def zoom():
    if request.method == 'GET':
        keywords = request.args.get("keywords")
        longitude = request.args.get("longitude")
        latitude = request.args.get("latitude")
        radius = request.args.get("radius")
        data = DataExtraction.anaylsis(keywords, longitude, latitude, radius)
        # for model in data:
        json_str = TweetsByProvinceEncoder().encode(data)

        j = json.dumps(json_str)
        # print("return data________ {}".format())

        return j

    return 'Nothing Happened!'


if __name__ == '__main__':
    app.run(debug=True)
