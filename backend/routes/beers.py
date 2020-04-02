from flask import Blueprint, jsonify

from domainTest.BeerService import BeerService

beers = Blueprint("beers", __name__, url_prefix="/")

beerService = BeerService()


@beers.route("beers/<beer_id>", methods=['GET'])
def getBeer(beer_id):
    beer = beerService.get(beer_id)
    print()
    return jsonify(beer.__dict__)
