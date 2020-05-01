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
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = 'SELECT * FROM Types WHERE type_id=' + str(type_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        typeInfos = cur.fetchone()
        return typeInfos
