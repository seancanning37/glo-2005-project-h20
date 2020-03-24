from flask import Flask, render_template
import pymysql
import pymysql.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'


def executeSqlScriptFromFile(filename):
    sqlCommands = getSqlCommands(filename)
    executeCommands(sqlCommands)


def getSqlCommands(filename):
    file = open(filename, "r")
    sqlFile = file.read()
    file.close()
    return sqlFile.split(';')


def executeCommands(sqlCommands):
    for command in sqlCommands:
        try:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD)
            cur = conn.cursor()
            print(command)
            cur.execute(command)
        except Exception as e:
            print(e)


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    executeSqlScriptFromFile('database/bd_init.sql')
    app.run()
