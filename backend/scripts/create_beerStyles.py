import json
from random import randint


with open("backend/json_files/beer_styles.json") as jsonfile:
    styles = json.load(jsonfile)

beerStyles = []

def create_beerStyles():
    for i in range(200):
        beerStyle = {
            "beer_id": i,
            "style_id": randint(1, len(styles))
        }
        beerStyles.append(beerStyle)
    return beerStyles
