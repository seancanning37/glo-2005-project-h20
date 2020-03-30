from faker import Faker
import json
from random import randint, choice

fake = Faker()

with open("backend/json_files/countries.json") as jsonfile:
    countries = json.load(jsonfile)

with open("backend/json_files/cities.json") as jsonfile:
    cities = json.load(jsonfile)


def create_brands():
    brands = []
    with open("backend/json_files/beer_brands.json") as jsonfile:
        data = json.load(jsonfile)
        for i, brand in enumerate(data):
            brand_infos = {
                'id': i,
                'name': brand['name'],
                'phone': generatePhoneNumber(),
                'address': getRandomStreetAddress(),
                'city': getRandomCity(),
                'country': getRandomCountry()
            }
            brands.append(brand_infos)
    return brands


def generatePhoneNumber():
    return "1-" + str(randint(100, 999)) + "-" + str(randint(100, 999)) + "-" + str(randint(1000, 9999))


def getRandomStreetAddress():
    address = fake.address()
    realAddress = address.split("\n")
    return realAddress[0]


def getRandomCountry():
    return choice(countries)['name']


def getRandomCity():
    return choice(cities)['name']

