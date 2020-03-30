from random import randint, choice, uniform
import json
from random_word import RandomWords
from faker import Faker

# url = "https://sandbox-api.brewerydb.com/v2/beers/?key=97891df5bfd71321fdf64fba603da425"

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
        beer = {
            "beer_id": i,
            "brand_id": randint(0, getNumberOfBrands()),
            "beer_name": generateRandomBeerName(),
            "abv": getRandomABV(),
            "ibu": getRandomIBU(),
            "volume": getRandomVolume(),
            "beer_price": getRandomPrice(),
            "description": getRandomDescription()
        }
        beers.append(beer)
    return beers


def getNumberOfBrands():
    with open("backend/json_files/beer_brands.json") as jsonfile:
        data = json.load(jsonfile)
    return len(data) - 1


def generateRandomBeerName():
    return choice(styles) + " " + fake.text().split(" ")[0] + " " + choice(types)


def getRandomABV():
    return round(uniform(0.1, 99.9), 1)


def getRandomIBU():
    return randint(0, 150)


def getRandomVolume():
    return randint(100, 2000)


def getRandomPrice():
    return round(uniform(0.99, 1000.00), 2)


def getRandomDescription():
    randomSize = randint(50, 150)
    myList = [word for word in fake.text()[0:randomSize].split(" ")]
    for i, word in enumerate(myList):
        if "\n" in word:
            myList[i] = " ".join(word.split("\n"))
    return " ".join(myList[:-1])

if __name__ == '__main__':
    print(getNumberOfBrands())
