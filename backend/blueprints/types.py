from flask import Blueprint, jsonify

from service.TypeService import TypeService

types = Blueprint("types", __name__, url_prefix="/")


@types.route("types/<type_id>", methods=['GET'])
def getType(type_id):
    typeService = TypeService()
    beerType = typeService.get(type_id)
    return jsonify(beerType.__dict__)
