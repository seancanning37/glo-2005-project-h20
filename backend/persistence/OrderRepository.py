import pymysql
import uuid


HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class OrderRepository:
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def getOrdersByCustomer(self, customer_id):
        cmd = f"SELECT * FROM Orders WHERE customer_id = '{customer_id}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        orders = cur.fetchall()
        return orders

    def getOrderItems(self, order_id):
        cmd = f"SELECT * FROM OrderItems WHERE order_id = '{order_id}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        items = cur.fetchall()
        return items

    def getOrderByID(self, order_id):
        cmd = f"SELECT * FROM Orders WHERE order_id = '{order_id}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        order = cur.fetchone()
        return order

    def buy(self, items, order, customer_id):
        cur = self.conn.cursor()

        order_id = uuid.uuid4()
        print(order_id)
        createOrderQuery = f"INSERT INTO Orders (order_id, customer_id, order_date, status, total_price, comment) VALUES ('{order_id}', '{customer_id}', '{order['order_date']}', '{order['status']}', '{order['total_price']}', '{order['comment']}');"
        cur.execute(createOrderQuery)

        for item in items:
            createOrderItemQuery = f"INSERT INTO OrderItems (order_id, beer_id, quantity) VALUES ('{order_id}', '{item['beer_id']}', '{item['quantity']}');"
            cur.execute(createOrderItemQuery)

        self.conn.commit()
