from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


app = Flask(__name__)
app.config.from_object(Config)
db.app = app
db.init_app(app)
migrate = Migrate(app, db)

app.run()
