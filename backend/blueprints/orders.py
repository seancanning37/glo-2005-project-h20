from flask import Blueprint, jsonify, request, Response

from service.OrderService import OrderService

beers = Blueprint("orders", __name__, url_prefix="/")


@beers.route("orders/<order_id>", methods=['GET'])
def getOrderByID(order_id):
    orderService = OrderService()
    order = orderService.getOrderByID(order_id)
    return jsonify(order.__dict__)


@beers.route("orders/<customer_id>", methods=['GET'])
def getOrdersByCustomer(customer_id):
    orderService = OrderService()
    orders = orderService.getOrdersByCustomer(customer_id)
    return jsonify(orders)


@beers.route("orders/<order_id>/items", methods=['GET'])
def getOrderItems(order_id):
    orderService = OrderService()
    order = orderService.getOrderItems(order_id)
    return jsonify(order.__dict__)


@beers.route("orders/buy", methods=['POST'])
def buy():
    items = request.json['items']
    customer_id = request.json['customer_id']
    orderService = OrderService()
    return orderService.buy(items, customer_id)

