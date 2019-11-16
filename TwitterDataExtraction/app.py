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


'''
Query from the URL parameters: ?key=value
'''
#
#
# @app.route('/query_example')
# def query_example():
#     lang = request.args.get('lang')
#     loc = request.args.get('location')
#     return "<h2> The language is {} </h2> <h2> The location is {} </h2>".format(lang, loc)
#

'''
Form data example
'''


# @app.route('/post_example', methods=['POST', 'GET'])
# def form_example():
#     if request.method == 'POST':
#         name = request.form.get('nickname')
#         school = request.form.get('school')
#         return "<h2> submitted done!</h2> <h2> Name: {}, School: {}</h2>".format(name, school)
#
#     return '''<form method="post" action="">
#                 <label for="hints">Input some words</label>
#                 <input type="text" name="nickname">
#                 <input type="text" name="school">
#                 <input type="submit" name="submit" value="search">
#               </form>
#             '''


'''
Json data example
'''


# @app.route('/json-example', methods=['POST'])
# def json_example():
#     req_data = request.get_json()
#     name = None
#
#     if 'name' in req_data:
#         name = req_data['name']
#
#     language = req_data['language']
#     boolean_test = req_data['boolean_test']
#     example = req_data['example'][2]  # list one
#     python_version = req_data['version_info']['python']  # nested json data
#     framework = req_data['Framework']
#
#     return '''
#     <h2>The name is {}.<br>
#     The language is {}.<br>
#     The framework is {}.<br>
#     The python_version is {}.<br>
#     The example is {}.<br>
#     The boolean_test is {}.</h2>
#     '''.format(name, language, framework, python_version, example, boolean_test)


'''
API example
'''

#
# @app.route('/api-example', methods=['POST', 'GET'])
# def api_example():
#     if request.method == 'POST':
#         j_data = request.get_json()
#         data = {
#             'name': j_data['Name'],
#             'boolean_val': j_data['Boolean_value'][0],
#             'version_info': j_data['Version'],
#             'users_info': j_data['Users']['Admin'],
#         }
#         return jsonify(data)
#     else:
#         return "<h1>Test GET method!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
