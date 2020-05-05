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
        self.conn.commit()
        brandInfos = cur.fetchone()
        return brandInfos

    def getAllBeers(self, brand_id):
        cmd = 'SELECT * FROM Beers INNER JOIN BeerPictures ON Beers.style_id = BeerPictures.style_id WHERE brand_id=' + \
            str(brand_id) + ';'
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        return cur.fetchall()

    def getAllBrands(self):
        cmd = "SELECT * FROM Brands;"
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        return cur.fetchall()
