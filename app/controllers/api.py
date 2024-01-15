from flask import Blueprint, jsonify, request

from app.errors import NotJsonError
from app.repositories.record_repository import RecordRepository

api = Blueprint('api', __name__, url_prefix='/api')


@api.errorhandler(NotJsonError)
def handle_not_json_error(error):
    return jsonify({'error': 'Invalid JSON'}), 400


@api.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({'error': 'Invalid data'}), 400


@api.get('/data')
def get_all_records():
    records = RecordRepository.get_records()
    return jsonify([record.serialize() for record in records])


@api.post('/data')
def add_record():
    if not request.is_json:
        raise NotJsonError

    data = request.get_json()

    record = RecordRepository.add_record(**data)
    if record is None:
        raise ValueError

    return jsonify({"id": record.id}), 200


@api.delete('/data/<int:record_id>')
def delete_record(record_id):
    if not RecordRepository.record_exists(record_id):
        return jsonify({'error': 'Record does not exist'}), 404

    RecordRepository.delete_record(record_id)
    return jsonify({'id': record_id}), 200
