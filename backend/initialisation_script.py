from flask import Flask, render_template
import pymysql
import pymysql.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

initScriptFilenames = [
    'database/db_init/init_tables.sql',
    'database/db_init/init_types.sql',
    'database/db_init/init_styles.sql',
    'database/db_init/init_brands.sql',
    'database/db_init/init_customers.sql',
    'database/db_init/init_beers.sql',
    'database/db_init/init_beerStyles.sql',
    'database/db_init/init_beerTypes.sql',
    'database/db_init/init_order_items.sql',
    'database/db_init/init_orders.sql',
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
            conn.commit()
        except Exception as e:
            print(e)


def executeCommands(sqlCommands):
    for command in sqlCommands[:-1]:
        try:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()
        except Exception as e:
            print(e)