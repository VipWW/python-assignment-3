from typing import List

from flask import current_app as app

from app.extensions import db
from app.models.record import Record


class RecordRepository:
    @staticmethod
    def add_record(**kwargs) -> Record:
        try:
            record = Record(**kwargs)
            db.session.add(record)
            db.session.commit()
            return record
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error adding record: {e}")
            return None

    @staticmethod
    def get_records() -> List[Record]:
        return Record.query.all()

    @staticmethod
    def get_record(record_id: str) -> Record:
        return Record.query.filter_by(id=record_id).first()

    @staticmethod
    def delete_record(record_id: str) -> None:
        record = Record.query.filter_by(id=record_id).first()
        db.session.delete(record)
        db.session.commit()

    @staticmethod
    def record_exists(record_id: str) -> bool:
        return Record.query.filter_by(id=record_id).first() is not None
