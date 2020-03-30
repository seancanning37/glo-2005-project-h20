import json
from random import randint


with open("backend/json_files/beer_types.json") as jsonfile:
    types = json.load(jsonfile)

beerTypes = []

def create_beerTypes():
    for i in range(200):
        beerType = {
            "beer_id": i,
            "type_id": randint(1, len(types))
        }
        beerTypes.append(beerType)
    return beerTypes
