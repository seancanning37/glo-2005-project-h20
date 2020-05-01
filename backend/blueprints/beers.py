from flask import Blueprint, jsonify

from service.BeerService import BeerService

beers = Blueprint("beers", __name__, url_prefix="/")


@beers.route("beers/<beer_id>", methods=['GET'])
def getBeer(beer_id):
    beerService = BeerService()
    beer = beerService.get(beer_id)
    return jsonify(beer.__dict__)


@beers.route("beers", methods=['GET'])
def getAllBeers():
    beerService = BeerService()
    beers = beerService.getAll()
    allBeers = jsonify([beer.__dict__ for beer in beers])
    return allBeers
