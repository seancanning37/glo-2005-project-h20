from flask import Blueprint, jsonify, request, Response
from domain.CustomerService import CustomerService

signup_blueprint = Blueprint("signup", __name__, url_prefix="/")
customerService = CustomerService()


@signup_blueprint.route("signup", methods=['POST'])
def signup():
    name, email, username, password = request.json["name"], request.json["email"], request.json["username"], request.json["password"]
    if not customerService.isEmailAlreadyUsed(email) and not customerService.isUsernameAlreadyUsed(username):
        customerService.addCustomer(name, email, username, password)
        return Response(status=201)
    response = jsonify({'Error': 'email or username already used'})
    return response, 400