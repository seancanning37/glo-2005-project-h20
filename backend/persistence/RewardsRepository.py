import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

SUCCESS_CODE = 0
ERROR_CODE = -1


class RewardsRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, customer_id):
        cmd = f"SELECT * FROM RewardCard C WHERE C.customer_id = '{customer_id}';"
        cur = self.conn.cursor()
        cur.execute(cmd)
        customerid_moneyearned = cur.fetchone()
        self.conn.commit()
        return customerid_moneyearned
