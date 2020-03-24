from flask import Flask, render_template
import pymysql
import pymysql.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

def createDatabaseScript(filename):
    sqlCommands = getSqlCommands(filename)
    executeCreateCommands(sqlCommands)

def executeSqlScriptFromFile(filename):
    sqlCommands = getSqlCommands(filename)
    executeCommands(sqlCommands)


def getSqlCommands(filename):
    file = open(filename, "r")
    sqlFile = file.read()
    file.close()
    return sqlFile.split(';')

def executeCreateCommands(sqlCommands):
    for command in sqlCommands[:-1]:
        try:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD)
            cur = conn.cursor()
            cur.execute(command)
        except Exception as e:
            print(e)


def executeCommands(sqlCommands):
    for command in sqlCommands[:-1]:
        try:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
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
    createDatabaseScript('database/create_database.sql')
    executeSqlScriptFromFile('database/bd_init.sql')
    app.run()
