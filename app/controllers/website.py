import requests
from flask import Blueprint, render_template, redirect, request

from app.repositories.record_repository import RecordRepository

website = Blueprint('website', __name__)


@website.get('/')
def index():
    data = RecordRepository.get_records()
    return render_template('index.html', rows=data)


@website.post('/delete/<int:record_id>')
def delete_record(record_id):
    if not RecordRepository.record_exists(record_id):
        return render_template('404.html', error_message='Record does not exist'), 404

    RecordRepository.delete_record(record_id)
    return redirect('/')


@website.get('/add')
def add_record():
    return render_template('add.html')


@website.post('/add')
def add_record_post():
    data = {
        'categorical_feature': request.form.get('categorical_feature'),
        'feature1': request.form.get('feature1'),
        'feature2': request.form.get('feature2'),
        'feature3': request.form.get('feature3'),
        'feature4': request.form.get('feature4'),
    }
    record = RecordRepository.add_record(**data)
    if record is None:
        return render_template('400.html', error_message='Invalid data'), 400
    return redirect('/')


@website.get('/xd')
def test_2():
    return render_template('404.html', error_message='Record does not exist'), 404


@website.get('/x')
def test():
    # make post requests to /api/data with JSON data. Remember about the
    # json header
    url = 'http://127.0.0.1:5000/api/data/6'
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
