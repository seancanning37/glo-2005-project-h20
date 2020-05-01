class OrderItem:
    def __init__(self, orderItemInfos):
		self.item_id = int(self.orderItemInfos[0])
		self.order_id = int(self.orderItemInfos[1])
		self.beer_id = int(self.orderItemInfos[2])
		self.quantity = int(self.orderItemInfos[3])
