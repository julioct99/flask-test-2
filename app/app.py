import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from app.security import authenticate, identity
from app.resources.user import UserRegister
from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList

from app.db import db

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///data.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "julio"
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, "/stores/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/items/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)

    if app.config["DEBUG"]:

        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
