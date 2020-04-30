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

    def isEmailAlreadyUsed(self, customerEmail):
        cmd = 'SELECT C.email FROM Customers C WHERE C.email = ' + '%s' + ';'
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd, customerEmail)
        return rows_count > 0

    def isUsernameAlreadyUsed(self, username):
        cmd = 'SELECT * FROM Customers C WHERE C.username = ' + '%s' + ';'
        cur = self.conn.cursor()
        rows_count = cur.execute(cmd, username)
        return rows_count > 0

    def addCustomer(self, name, email, username, password):
        try:
            cmd = "INSERT INTO Customers (name, email, username, password) VALUES (%s, %s, %s, %s)"
            cur = self.conn.cursor()
            customerInformations = (name, email, username, password)
            cur.execute(cmd, customerInformations)
            self.conn.commit()
            return SUCCESS_CODE
        except pymysql.IntegrityError as error:
            return ERROR_CODE

    def areLoginInformationsValid(self, email, password):
        cmd = 'SELECT * FROM Customers C WHERE C.email = (%s) AND C.password = (%s);'
        cur = self.conn.cursor()
        loginInfo = (email, password)
        rows_count = cur.execute(cmd, loginInfo)
        return rows_count > 0

    def getCustomerIdFromEmail(self, email):
        cmd = 'SELECT C.id FROM CUSTOMERS C WHERE C.email = (%s)'
        cur = self.conn.cursor()
        cur.execute(cmd, email)
        customerId = cur.fetchone()[0]
        return customerId

    def getCustomerFromId(self, customerId):
        cmd = 'SELECT * FROM CUSTOMERS C WHERE C.id = (%s)'
        cur = self.conn.cursor()
        cur.execute(cmd, customerId)
        customerInfo = cur.fetchone()
        return customerInfo

    def updateCustomerName(self, customerId, newName):
        try:
            cmd = 'UPDATE CUSTOMERS C SET C.name = (%s) where C.id = (%s)'
            customerInfos = (newName, customerId)
            cur = self.conn.cursor()
            cur.execute(cmd, customerInfos)
            self.conn.commit()
            return SUCCESS_CODE
        except pymysql.IntegrityError as error:
            return ERROR_CODE

    def getCustomerHashedPasswordFromId(self, customerId):
        cmd = 'SELECT C.password FROM CUSTOMERS C WHERE C.id = (%s)'
        cur = self.conn.cursor()
        cur.execute(cmd, customerId)
        hashedPassword = cur.fetchone()[0]
        return hashedPassword


