import pymysql
from ..domain.Beer import Beer

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)


class BeerRepository:
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, beer_id):
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
        cmd = 'SELECT * FROM Beers WHERE beer_id=' + str(beer_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        beerInfos = cur.fetchone()
        return beerInfos




