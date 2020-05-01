import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class BeerRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, beer_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = 'SELECT * FROM Beers WHERE beer_id=' + str(beer_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        beerInfos = cur.fetchone()
        return beerInfos

    def getBeerURLFromStyleId(self, type_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = 'SELECT picture_url FROM BeerPictures WHERE style_id=' + \
            str(type_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        pictureUrl = cur.fetchone()
        return pictureUrl
