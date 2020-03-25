from flask import Flask, render_template
import pymysql
import pymysql.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

initScriptFilenames = [
    'database/db_init_scripts/init_tables.sql',
    'database/db_init_scripts/init_types.sql',
    'database/db_init_scripts/init_styles.sql',
    'database/db_init_scripts/init_brands.sql',
    'database/db_init_scripts/init_customers.sql',
    'database/db_init_scripts/init_beers.sql',
    'database/db_init_scripts/init_beerStyles.sql',
    'database/db_init_scripts/init_beerTypes.sql',
    'database/db_init_scripts/init_order_items.sql',
    'database/db_init_scripts/init_orders.sql',
]


def createDatabaseScript(filename):
    sqlCommands = getSqlCommands(filename)
    executeCreateCommands(sqlCommands)


def runAllInitScript():
    for filename in initScriptFilenames:
        executeSqlScriptFromFile(filename)


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
    createDatabaseScript('database/db_init_scripts/create_database.sql')
    runAllInitScript()
    app.run()
