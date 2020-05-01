from flask import Blueprint, jsonify

from service.BrandService import BrandService

brands = Blueprint("brands", __name__, url_prefix="/")


@brands.route("brands/<brand_id>", methods=['GET'])
def getBrand(brand_id):
    brandservice = BrandService()
    beer = brandservice.get(brand_id)
    return jsonify(beer.__dict__)
