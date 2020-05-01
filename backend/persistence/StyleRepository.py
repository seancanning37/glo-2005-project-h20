import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


class StyleRepository:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, db=DATABASE)

    def get(self, style_id):
        conn = pymysql.connect(host=HOST, user=USER,
                               password=PASSWORD, db=DATABASE)
        cmd = 'SELECT * FROM Styles WHERE style_id=' + str(style_id) + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        styleInfos = cur.fetchone()
        return styleInfos
