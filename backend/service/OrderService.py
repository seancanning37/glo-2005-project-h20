from domain.Order import Order
from domain.OrderItem import OrderItem
from persistence import OrderRepository

class OrderService:
    def __init__(self):
        self.OrderRepository = OrderRepository.OrderRepository()

    def getOrdersByCustomer(self, customer_id):
        return [ Order(orderInfo) for orderInfo in self.OrderRepository.getOrdersByCustomer(customer_id) ]

    def getOrderItems(self, order_id):
        return [ OrderItem(orderItemInfo) for orderItemInfo in self.OrderRepository.getOrderItems(order_id) ]

    def getOrderByID(self, order_id):
        return Order(self.OrderRepository.getOrderByID(order_id))

    def buy(self, items, order, customer_id):
        self.OrderRepository(items, order, customer_id)
