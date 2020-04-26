import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

EMPTY_SET = -1



class CustomerRepository:
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def getCustomerFromEmail(self, customerEmail):
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
        cmd = 'SELECT C.email FROM Customers C WHERE C.email = ' + '%s' + ';'
        cur = conn.cursor()
        rows_count = cur.execute(cmd, customerEmail)
        if rows_count > 0:
            return cur.fetchone()
        return EMPTY_SET
