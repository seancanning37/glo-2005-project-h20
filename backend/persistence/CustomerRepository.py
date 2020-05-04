import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

SUCCESS_CODE = 0
ERROR_CODE = -1


class CustomerRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def isEmailAlreadyUsed(self, customerEmail):
        cmd = f"SELECT C.email FROM Customers C WHERE C.email = '{customerEmail}';"
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd)
        self.conn.commit()
        return rows_count > 0

    def isUsernameAlreadyUsed(self, username):
        cmd = f"SELECT * FROM Customers C WHERE C.username = '{username}';"
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd)
        self.conn.commit()
        return rows_count > 0

    def addCustomer(self, name, email, username, password):
        try:
            self.insertCustomer(name, email, username)
            customer_id = self.getCustomerFromId(name, email)
            self.insertPassword(customer_id, password)
            return SUCCESS_CODE
        except pymysql.IntegrityError as error:
            return ERROR_CODE

    def getCustomerId(self, name, email):
        cmd = f"SELECT C.customer_id FROM Customers C WHERE C.name = {name} and C.email = {email};"
        cur = self.conn.cursor()
        cur.execute(cmd)
        return cur.fetchone()

    def insertCustomer(self, name, email, username):
        cmd = "INSERT INTO Customers (name, email, username) VALUES (%s, %s, %s);"
        customerInformations = (name, email, username)
        cur = self.conn.cursor()
        cur.execute(cmd, customerInformations)
        self.conn.commit()

    def insertPassword(self, customer_id, password):
        cmd = "INSERT INTO Passwords (customer_id, password) VALUES (%s, %s)"
        passwordInformations = (customer_id, password)
        cur = self.conn.cursor()
        cur.execute(cmd, passwordInformations)
        self.conn.commit()

    def areLoginInformationsValid(self, email, password):
        cmd = f"SELECT * FROM Customers C WHERE C.email = '{email}' AND C.password = '{password}';"
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd)
        self.conn.commit()
        return rows_count > 0

    def getCustomerIdFromEmail(self, email):
        cmd = f"SELECT C.id FROM CUSTOMERS C WHERE C.email = '{email}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        customerId = cur.fetchone()[0]
        return customerId

    def getCustomerFromId(self, customerId):
        cmd = f"SELECT * FROM CUSTOMERS C WHERE C.id = '{customerId}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        customerInfo = cur.fetchone()
        return customerInfo

    def updateCustomerName(self, customerId, newName):
        try:
            cmd = f"UPDATE CUSTOMERS C SET C.name = '{newName}' where C.id = '{customerId}';"
            cur = self.conn.cursor()
            cur.execute(cmd)
            self.conn.commit()
            return SUCCESS_CODE
        except pymysql.IntegrityError as error:
            return ERROR_CODE

    def getCustomerHashedPasswordFromId(self, customerId):
        cmd = f"SELECT C.password FROM CUSTOMERS C WHERE C.id = '{customerId}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        hashedPassword = cur.fetchone()[0]
        return hashedPassword

    def updateCustomer(self, customerId, parameters):
        try:
            for attribute in parameters:
                cmd = f"UPDATE CUSTOMERS C SET C.{attribute} = '{parameters[attribute]}' where C.id = '{customerId}';"
                cur = self.conn.cursor()
                cur.execute(cmd)
                self.conn.commit()
        except pymysql.IntegrityError as error:
            return ERROR_CODE
        self.conn.commit()
        return SUCCESS_CODE


