#from domain.Order import Order
from persistence import OrderRepository


class OrderService:
    def __init__(self):
        self.OrderRepository = OrderRepository.OrderRepository()

    def getOrdersByCustomer(self, customer_id):
        return self.OrderRepository.getOrdersByCustomer(customer_id)

    def getOrderItems(self, order_id):
        return self.OrderRepository.getOrderItems(order_id)

    def getOrderByID(self, order_id):
        return self.OrderRepository.getOrderByID(order_id)

    def buy(self, items, customer_id):
        return
