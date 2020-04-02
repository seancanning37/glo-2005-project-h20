from flask import Blueprint, jsonify

from domain.BeerService import BeerService

beers = Blueprint("beers", __name__, url_prefix="/")



@beers.route("beers/<beer_id>", methods=['GET'])
def getBeer(beer_id):
    beerService = BeerService()
    beer = beerService.get(beer_id)
    return jsonify(beer.__dict__)
