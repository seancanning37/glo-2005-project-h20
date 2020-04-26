import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

SUCCESS_CODE = 0
ERROR_CODE = -1

class CustomerRepository:
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def getCustomerFromEmail(self, customerEmail):
        cmd = 'SELECT C.email FROM Customers C WHERE C.email = ' + '%s' + ';'
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd, customerEmail)
        if rows_count > 0:
            return cur.fetchone()
        return ERROR_CODE

    def addCustomer(self, name, email, username, password):
        cmd = "INSERT INTO Customers (name, email, username, password) VALUES (%s, %s, %s, %s)"
        cur = self.conn.cursor()
        customerInformations = (name, email, username, password)
        cur.execute(cmd, customerInformations)
        self.conn.commit()
        return SUCCESS_CODE

