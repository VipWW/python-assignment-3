from app.extensions import db


class Record(db.Model):
    __tablename__ = 'Records'
    id = db.Column(db.Integer, primary_key=True)
    feature1 = db.Column(db.Float, nullable=False)  # age
    feature2 = db.Column(db.Float, nullable=False)  # capital gain
    feature3 = db.Column(db.Float, nullable=False)  # capital loss
    feature4 = db.Column(db.Float, nullable=False)  # income
    categorical_feature = db.Column(db.Integer, nullable=False)  # hours per
    # week

    def serialize(self):
        return {
            'id': self.id,
            'feature1': self.feature1,
            'feature2': self.feature2,
            'feature3': self.feature3,
            'feature4': self.feature4,
            'categorical_feature': self.categorical_feature
        }
