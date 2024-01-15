import sqlalchemy.exc
from flask import Flask

from app.extensions import db

APP_CONFIG = {
    "SQLALCHEMY_DATABASE_URI": "sqlite:///database.db",
}


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_mapping(APP_CONFIG)

    db.init_app(app)

    # controllers
    from app.controllers.website import website
    app.register_blueprint(website)

    from app.controllers.api import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()
        with open('./data_ml.csv', 'r') as file:
            import pandas as pd
            data_df = pd.read_csv(file)
            try:
                data_df.to_sql('Records', con=db.engine, index=False,
                               if_exists='append',
                               )

            except sqlalchemy.exc.IntegrityError as e:
                pass  # data already exists

    return app
