# External modules
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
ENV = os.getenv("FLASK_ENV", "dev")

if ENV == "dev":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_DATABASE_URL", "sqlite:///library.db")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQL_DATABASE_URL"]
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from library.routes import routes, book_routes, member_routes, transaction_routes 
