from random import randint, choice, uniform
import json
from faker import Faker

fake = Faker()

styles = [
    'Amber',
    'Blonde',
    'Brown',
    'Cream',
    'Dark',
    'Pale',
    'Strong',
    'Wheat',
    'Red',
    'Lime',
    'Pilsner',
    'Golden',
    'Fruit',
    'Honey'
]

types = [
    'Ale',
    'Lager',
    'Malt',
    'Stout'
]

beers = []


def create_beers():
    for i in range(200):
        style_id = getRandomStyleID()
        type_id = getRandomTypeID()
        beer = {
            "beer_id": i,
            "brand_id": randint(0, getNumberOfBrands()),
            "beer_name": generateRandomBeerName(styles[style_id - 1], types[type_id - 1]),
            "abv": getRandomABV(),
            "ibu": getRandomIBU(),
            "volume": getRandomVolume(),
            "style_id": style_id,
            "type_id": type_id,
            "beer_price": getRandomPrice(),
            "disponibility": getRandomDisponibility(),
            "description": getRandomDescription()
        }
        beers.append(beer)
    return beers


def getNumberOfBrands():
    with open("../json_files/beer_brands.json") as jsonfile:
        data = json.load(jsonfile)
    return len(data) - 1


def generateRandomBeerName(style, beerType):
    return style + " " + fake.text().split(" ")[0] + " " + beerType


def getRandomABV():
    return round(uniform(0.1, 30), 1)


def getRandomIBU():
    return randint(0, 150)


def getRandomVolume():
    return randint(100, 1000)


def getRandomPrice():
    return round(uniform(2.50, 35.0), 2)


def getRandomStyleID():
    with open("../json_files/beer_styles.json") as jsonFile:
        data = json.load(jsonFile)
    return randint(1, len(data))


def getRandomTypeID():
    with open("../json_files/beer_types.json") as jsonFile:
        data = json.load(jsonFile)
    return randint(1, len(data))


def getRandomDisponibility():
    return randint(0, 2000)


def getRandomDescription():
    randomSize = randint(50, 100)
    myList = [word for word in fake.text()[0:randomSize].split(" ")]
    for i, word in enumerate(myList):
        if "\n" in word:
            myList[i] = " ".join(word.split("\n"))
    return " ".join(myList[:-1])


if __name__ == '__main__':
    with open("../json_files/beers.json", 'w') as file:
        json.dump(create_beers(), file)
