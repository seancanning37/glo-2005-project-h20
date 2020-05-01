from flask import Blueprint, jsonify

from service.OrderService import OrderService

beers = Blueprint("orders", __name__, url_prefix="/")


@beers.route("orders/<order_id>", methods=['GET'])
def getOrder(order_id):
    orderService = OrderService()
    order = orderService.get(order_id)
    return jsonify(order.__dict__)
