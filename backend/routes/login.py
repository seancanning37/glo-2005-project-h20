from flask import Blueprint, jsonify, request, Response
from domain.CustomerService import CustomerService

login_blueprint = Blueprint("login", __name__, url_prefix="/")
customerService = CustomerService()


@login_blueprint.route("login", methods=['POST'])
def login():
    email, password = request.json["email"], request.json["password"]
    if customerService.areLoginInformationsValid(email, password):
        return Response(status=201)
    response = jsonify({'Error': 'Email or password invalid'})
    return response, 400