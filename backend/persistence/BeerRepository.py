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
        cmd = 'SELECT * FROM Beers INNER JOIN BeerPictures ON Beers.style_id = BeerPictures.style_id WHERE beer_id=' + \
            str(beer_id)
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        beerInfos = cur.fetchone()
        return beerInfos

    def getAll(self):
        cmd = 'SELECT * FROM Beers INNER JOIN BeerPictures ON Beers.style_id = BeerPictures.style_id;'
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        return cur.fetchall()


if __name__ == '__main__':
    beerRepo = BeerRepository()
    beerRepo.getAll()
