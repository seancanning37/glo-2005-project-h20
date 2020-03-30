import pymysql
import pymysql.cursors
from .scripts.create_brands import create_brands
from .scripts.create_beers import create_beers
from .scripts.create_beerStyles import create_beerStyles
from .scripts.create_beerTypes import create_beerTypes

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
    populateBeers()
    populateBeerStyles()
    populateBeerTypes()


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
            add_brand = "INSERT INTO Brands" \
                        "(brand_id, brand_name, brand_phone, brand_address, brand_city, brand_country)" \
                        "VALUES (%s, %s, %s, %s, %s, %s)"
            brand_data = (brand['id'], brand['name'], brand['phone'], brand['address'], brand['city'], brand['country'])
            cur.execute(add_brand, brand_data)
            conn.commit()
    except Exception as e:
        print(e)


def populateBeers():
    beers = create_beers()
    try:
        for beer in beers:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            add_beer = "INSERT INTO Beers" \
                       "(beer_id, brand_id, beer_name, abv, ibu, volume, beer_price, description)" \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            beer_data = (
                beer['beer_id'], beer['brand_id'], beer['beer_name'], beer['abv'], beer['ibu'], beer['volume'],
                beer['beer_price'], beer['description'])
            cur.execute(add_beer, beer_data)
            conn.commit()
    except Exception as e:
        print(e)


def populateBeerStyles():
    beerStyles = create_beerStyles()
    try:
        for beerStyle in beerStyles:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            add_beer = "INSERT INTO BeerStyles" \
                       "(beer_id, style_id)" \
                       "VALUES (%s, %s)"
            beerStyle_data = (beerStyle['beer_id'], beerStyle['style_id'])
            cur.execute(add_beer, beerStyle_data)
            conn.commit()
    except Exception as e:
        print(e)


def populateBeerTypes():
    beerTypes = create_beerTypes()
    try:
        for beerType in beerTypes:
            conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DATABASE)
            cur = conn.cursor()
            add_beer = "INSERT INTO BeerTypes" \
                       "(beer_id, type_id)" \
                       "VALUES (%s, %s)"
            beerType_data = (beerType['beer_id'], beerType['type_id'])
            cur.execute(add_beer, beerType_data)
            conn.commit()
    except Exception as e:
        print(e)
