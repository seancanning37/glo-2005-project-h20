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
        cmd = 'SELECT * FROM Beers WHERE beer_id=' + str(beer_id) + ';'
        cur = self.conn.cursor()
        cur.execute(cmd)
        beerInfos = cur.fetchone()
        return beerInfos

    def getBeerURLFromStyleId(self, type_id):
        cmd = 'SELECT picture_url FROM BeerPictures WHERE style_id=' + \
            str(type_id) + ';'
        cur = self.conn.cursor()
        cur.execute(cmd)
        pictureUrl = cur.fetchone()
        return pictureUrl

    def getAll(self):
        cmd = 'SELECT * FROM Beers;'
        cur = self.conn.cursor()
        cur.execute(cmd)
        return cur.fetchall()

if __name__ == '__main__':
    beerRepo = BeerRepository()
    beerRepo.getAll()
