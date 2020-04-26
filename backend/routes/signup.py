from flask import Blueprint, jsonify, request
from domain.CustomerService import CustomerService

signup_blueprint = Blueprint("signup", __name__, url_prefix="/")
customerService = CustomerService()


@signup_blueprint.route("signup", methods=['POST'])
def signup():
    email = request.json["email"]
    if not customerService.isEmailAlreadyUsed(email):
        return jsonify("email is not used")
    return jsonify("email already used")


def isUserAlreadyExist():
    return True;
