import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class BrandRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, brand_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = 'SELECT * FROM Brands WHERE brand_id=' + str(brand_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        brandInfos = cur.fetchone()
        return brandInfos
