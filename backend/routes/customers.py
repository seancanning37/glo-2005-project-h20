from flask import Blueprint, jsonify

from domain.CustomerService import CustomerService

customers_blueprint = Blueprint("customers", __name__, url_prefix="/")


@customers_blueprint.route("customers/<customer_id>", methods=['GET'])
def getCustomer(customer_id):
    customerService = CustomerService()
    customer = customerService.getCustomerFromId(customer_id)
    return jsonify(customer.__dict__)
