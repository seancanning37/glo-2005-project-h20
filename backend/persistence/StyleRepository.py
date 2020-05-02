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
        cmd = 'SELECT * FROM Styles WHERE style_id=' + str(style_id) + ';'
        cur = self.conn.cursor()
        cur.execute(cmd)
        self.conn.commit()
        styleInfos = cur.fetchone()
        return styleInfos
