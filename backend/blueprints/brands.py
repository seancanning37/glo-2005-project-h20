from flask import Blueprint, jsonify

from service.BrandService import BrandService

brands = Blueprint("brands", __name__, url_prefix="/")


@brands.route("brands/<brand_id>", methods=['GET'])
def getBrand(brand_id):
    brandservice = BrandService()
    brand = brandservice.get(brand_id)
    return jsonify(brand.__dict__)


@brands.route("brands/<brand_id>/beers", methods=['GET'])
def getAllBeers(brand_id):
    brandService = BrandService()
    beers = brandService.getAllBeers(brand_id)
    allBeers = jsonify([beer.__dict__ for beer in beers])
    return allBeers

@brands.route("brands", methods=['GET'])
def getAllBrands():
    brandservice = BrandService()
    brands = brandservice.getAllBrands()
    return jsonify([brand.__dict__ for brand in brands])