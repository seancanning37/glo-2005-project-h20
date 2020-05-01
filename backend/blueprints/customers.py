from flask import Blueprint, jsonify, request

from service.CustomerService import CustomerService

customers_blueprint = Blueprint("customers", __name__, url_prefix="/")


@customers_blueprint.route("customers/<customer_id>", methods=['GET'])
def getCustomer(customer_id):
    customerService = CustomerService()
    customer = customerService.getCustomerFromId(customer_id)
    return jsonify(customer.__dict__)


@customers_blueprint.route("customers/<customer_id>/modify", methods=['PUT'])
def updateCustomerName(customer_id):
    customerService = CustomerService()
    newParameters = request.json
    customerService.updateCustomer(customer_id, newParameters)
    response = jsonify({'message': 'update successful'})
    return response, 200
