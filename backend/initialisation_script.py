import pymysql
import pymysql.cursors
from .scripts.generate_brands import create_brands

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

initScriptFilenames = [
    'database/db_init/init_tables.sql',
    'database/db_init/init_types.sql',
    'database/db_init/init_styles.sql'
]


def createDatabaseScript(filename):
    sqlCommands = getSqlCommands(filename)
    executeCreateCommands(sqlCommands)


def runAllInitScript():
    for filename in initScriptFilenames:
        executeSqlScriptFromFile(filename)
    populateBrands()


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


def populateBrands():
    brands = create_brands()
    try:
        for brand in brands:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            print(brand)
            add_brand = "INSERT INTO Brands" \
                        "(brand_id, brand_name, brand_phone, brand_address, brand_city, brand_country)" \
                        "VALUES (%s, %s, %s, %s, %s, %s)"
            brand_data = (brand['id'], brand['name'], brand['phone'], brand['address'], brand['city'], brand['country'])
            cur.execute(add_brand, brand_data)
            conn.commit()
    except Exception as e:
        print(e)
