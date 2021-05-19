from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from app.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store id"
    )

    def get(self, name):
        try:
            item = ItemModel.find_item_by_name(name)
            if item:
                return item.json()
            return {"message": "Item not found"}, 404
        except:
            return {"Message": "An error occured while getting the item"}

    def put(self, name):

        data = Item.parser.parse_args()

        try:
            item = ItemModel.find_item_by_name(name)
            if not item:
                item = ItemModel(**data)
            else:
                item.price = data["price"]
            item.save()

            return item.json()
        except:
            return {"message": "There was an error updating the item"}, 500

    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete()
            return {"message": "Item deleted successfully"}
        return {"message": "The item was not found"}, 404


class ItemList(Resource):
    def get(self):
        return {"items": [i.json() for i in ItemModel.query.all()]}

    def post(self):
        data = Item.parser.parse_args()

        if ItemModel.find_item_by_name(data["name"]):
            return {"message": "Error: Item already exists"}, 409

        item = ItemModel(**data)
        item.save()

        return item.json(), 201
