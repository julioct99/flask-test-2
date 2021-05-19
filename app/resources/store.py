from flask_restful import Resource, reqparse
from app.models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store already exists"}, 409

        store = StoreModel(name)
        try:
            store.save()
        except:
            return {"message: An error occurered while creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
            return {"message": "Store deleted"}
        return {"message": "Store was not found"}, 404


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
