from flask import Blueprint, jsonify, request, session
from uuid import uuid4
from service.CustomerService import CustomerService

login_blueprint = Blueprint("login", __name__, url_prefix="/")
customerService = CustomerService()


@login_blueprint.route("login", methods=['POST'])
def login():
    email, password = request.json["email"], request.json["password"]
    if customerService.areLoginInformationsValid(email, password):
        token = uuid4()
        session["email"] = {"token": token, "customer_id" : customerService.getCustomerIdFromEmail(email), "cart" : []}
        response = jsonify(session["email"])
        return response, 201
    response = jsonify({'Error': 'Email or password invalid'})
    return response, 400