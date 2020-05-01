class Order:
	def __init__(self, orderInfo):
		self.order_id = orderInfo[0]
		self.customer_id =int(orderInfo[1])
		self.order_date = orderInfo[2]
		self.status = orderInfo[3]
		self.total_price = float(orderInfo[4])
		self.comment = orderInfo[5]

