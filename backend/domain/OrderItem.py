class OrderItem:
	def __init__(self, orderItemInfos):
		self.item_id = int(orderItemInfos[0])
		self.order_id = orderItemInfos[1]
		self.beer_id = int(orderItemInfos[2])
		self.quantity = int(orderItemInfos[3])
