from flask import Blueprint, jsonify, request, Response

from service.OrderService import OrderService

orders = Blueprint("orders", __name__, url_prefix="/")


@orders.route("orders/<order_id>", methods=['GET'])
def getOrderByID(order_id):
    orderService = OrderService()
    order = orderService.getOrderByID(order_id).__dict__
    return jsonify(order)


@orders.route("orders/customer/<customer_id>", methods=['GET'])
def getOrdersByCustomer(customer_id):
    orderService = OrderService()
    orders = [ order.__dict__ for order in orderService.getOrdersByCustomer(customer_id) ]
    return jsonify(orders)


@orders.route("orders/<order_id>/items", methods=['GET'])
def getOrderItems(order_id):
    orderService = OrderService()
    items = [ item.__dict__ for item in orderService.getOrderItems(order_id) ]
    return jsonify(items)


@orders.route("orders/buy", methods=['POST'])
def buy():
    print("Ben wtf")
    items = request.json['items']
    order = request.json['order']
    customer_id = request.json['customer_id']
    orderService = OrderService()
    orderService.buy(items, order, customer_id)
    return Response(status=201)