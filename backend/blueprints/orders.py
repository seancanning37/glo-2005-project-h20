from flask import Blueprint, jsonify, request, Response

from service.OrderService import OrderService

beers = Blueprint("orders", __name__, url_prefix="/")


@beers.route("orders/<order_id>", methods=['GET'])
def getOrderByID(order_id):
    orderService = OrderService()
    order = orderService.getOrderByID(order_id).__dict__
    return jsonify(order)


@beers.route("orders/customer/<customer_id>", methods=['GET'])
def getOrdersByCustomer(customer_id):
    orderService = OrderService()
    orders = [ order.__dict__ for order in orderService.getOrdersByCustomer(customer_id) ]
    return jsonify(orders)


@beers.route("orders/<order_id>/items", methods=['GET'])
def getOrderItems(order_id):
    orderService = OrderService()
    items = [ item.__dict__ for item in orderService.getOrderItems(order_id) ]
    return jsonify(items)


@beers.route("orders/buy", methods=['POST'])
def buy():
    items = request.json['items']
    order = request.json['order']
    customer_id = request.json['customer_id']
    orderService = OrderService()
    orderService.buy(items, order, customer_id)
    return Response(status=201)

