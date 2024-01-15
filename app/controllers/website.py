import requests
from flask import Blueprint

website = Blueprint('website', __name__)


@website.get('/')
def index():
    return 'Hello World!'


@website.get('/x')
def test():
    # make post requests to /api/data with JSON data. Remember about the
    # json header
    url = 'http://127.0.0.1:5000/api/data/10000000'
    # data = {
    #     'feature1': '10',
    #     'feature2': '10',
    #     'feature3': '10',
    #     'feature4': '10',
    #     'categorical_feature': '10',
    # }
    # r = requests.post(url, json=data, headers={'content-type': 'application/json'})
    r = requests.delete(url)
    return r.text
