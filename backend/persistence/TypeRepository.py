import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class TypeRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, type_id):
        cmd = 'SELECT * FROM Types WHERE type_id=' + str(type_id) + ';'
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        typeInfos = cur.fetchone()
        return typeInfos
