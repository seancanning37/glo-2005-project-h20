import pymysql
import pymysql.cursors
import json

HOST = 'localhost'
USER = 'root'
PASSWORD = 'glo2005xD'
DATABASE = 'glo2005'

initScriptFilenames = [
    '../database/db_init/init_tables.sql',
    '../database/db_init/init_types.sql',
    '../database/db_init/init_styles.sql',
    '../database/db_init/init_beerPictures.sql'
]


def createDatabaseScript(filename):
    sqlCommands = getSqlCommands(filename)
    executeCreateCommands(sqlCommands)


def runAllInitScript():
    for filename in initScriptFilenames:
        executeSqlScriptFromFile(filename)
    populateBrands()
    populateBeers()
    createTriggers()


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
            conn = pymysql.connect(host=HOST, user=USER,
                                   password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()
        except Exception as e:
            print(e)


def loadJsonFromFilePath(filepath):
    with open(filepath, "r") as jsonFile:
        return json.load(jsonFile)


def createTriggers():
    with open("../database/db_init/init_triggers.sql", 'r') as sqlFile:
        commands = sqlFile.read().split("//")

    commandsWithDelimiters = []
    for command in commands[:-1]:
        commandsWithDelimiters.append("DELIMITER //")
        commandsWithDelimiters.append(command + "//")
        commandsWithDelimiters.append("DELIMITER ;")

    executeCommands(commands)


def populateBrands():
    brands = loadJsonFromFilePath("json_files/brands.json")
    try:
        for brand in brands:
            conn = pymysql.connect(host=HOST, user=USER,
                                   password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            add_brand = "INSERT INTO Brands" \
                        "(brand_id, brand_name, brand_phone, brand_address, brand_city, brand_country)" \
                        "VALUES (%s, %s, %s, %s, %s, %s)"
            brand_data = (brand['id'], brand['name'], brand['phone'],
                          brand['address'], brand['city'], brand['country'])
            cur.execute(add_brand, brand_data)
            conn.commit()
    except Exception as e:
        print(e)


beersIdWithStyleId = {}
beersIdWithTypeId = {}


def populateBeers():
    beers = loadJsonFromFilePath("json_files/beers.json")
    try:
        for beer in beers:
            beersIdWithStyleId[beer['beer_id']] = beer['style_id']
            beersIdWithTypeId[beer['beer_id']] = beer['type_id']
            conn = pymysql.connect(host=HOST, user=USER,
                                   password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            add_beer = "INSERT INTO Beers" \
                       "(beer_id, brand_id, beer_name, abv, ibu, volume, style_id, type_id, beer_price, disponibility, description)" \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            beer_data = (
                beer['beer_id'], beer['brand_id'], beer['beer_name'], beer['abv'], beer['ibu'], beer['volume'],
                beer["style_id"], beer["type_id"],
                beer['beer_price'], beer['disponibility'], beer['description'])
            cur.execute(add_beer, beer_data)
            conn.commit()
    except Exception as e:
        print(e)
