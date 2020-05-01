import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class OrderRepository:
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def getOrdersByCustomer(self, customer_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = f"SELECT * FROM Orders WHERE customer_id = '{customer_id}';"
        cur = conn.cursor()
        cur.execute(cmd)
        orders = cur.fetchall()
        return orders

    def getOrderItems(self, order_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = f"SELECT * FROM OrderItems WHERE order_id = '{order_id}';"
        cur = conn.cursor()
        cur.execute(cmd)
        items = cur.fetchall()
        return items

    def getOrderByID(self, order_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = f"SELECT * FROM Orders WHERE order_id = '{order_id}';"
        cur = conn.cursor()
        cur.execute(cmd)
        order = cur.fetchone()
        return order

    def buy(self, items, customer_id):
        return
