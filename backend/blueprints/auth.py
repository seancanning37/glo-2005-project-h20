from flask import Blueprint, jsonify, request
from uuid import uuid4
from service.CustomerService import CustomerService

login_blueprint = Blueprint("login", __name__, url_prefix="/")
customerService = CustomerService()

session = {}

@login_blueprint.route("login", methods=['POST'])
def login():
    email, password = request.json["email"], request.json["password"]
    if customerService.areLoginInformationsValid(email, password):
        token = uuid4()
        session[str(token)] = {"token": token, "customer_id" : customerService.getCustomerIdFromEmail(email), "cart" : []}
        response = jsonify(session[str(token)])
        return response, 201
    response = jsonify({'Error': 'Email or password invalid'})
    return response, 400


@login_blueprint.route("logout", methods=['POST'])
def logout():
    token = request.json["token"]
    session.pop(token)
    return session


@login_blueprint.route("tokenInfo", methods=['GET'])
def getTokenInfo():
    token = request.headers["token"]
    customerId = session[token]["customer_id"]
    tokenInfo = {"token": token, "customer_id": customerId, "email": customerService.getCustomerFromId(customerId).email}
    return tokenInfo, 200
