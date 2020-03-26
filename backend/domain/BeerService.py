from .Beer import Beer
from ..persistence import BeerRepository


def createBeerFromCursorInfos(beerInfos):
    beer = Beer()
    beer.id = beerInfos[0]
    beer.brand_id = beerInfos[1]
    beer.name = beerInfos[2]
    beer.abv = float(beerInfos[3])
    beer.ibu = beerInfos[4]
    beer.volume = beerInfos[5]
    beer.country = beerInfos[6]
    beer.price = float(beerInfos[7])
    beer.description = beerInfos[8]
    return beer


class BeerService:
    def __init__(self):
        self.beerRepository = BeerRepository.BeerRepository()

    def get(self, beer_id):
        beer = createBeerFromCursorInfos(self.beerRepository.get(beer_id))
        return beer
