from domain.Beer import Beer
from persistence import BeerRepository


def createBeerFromCursorInfos(beerInfos):
    beer = Beer()
    beer.id = beerInfos[0]
    beer.brand_id = beerInfos[1]
    beer.name = beerInfos[2]
    beer.abv = str(beerInfos[3])
    beer.ibu = beerInfos[4]
    beer.volume = beerInfos[5]
    beer.style_id = beerInfos[6]
    beer.type_id = beerInfos[7]
    beer.price = str(beerInfos[8])
    beer.disponibility = beerInfos[9]
    beer.description = beerInfos[10]
    return beer


class BeerService:
    def __init__(self):
        self.beerRepository = BeerRepository.BeerRepository()

    def get(self, beer_id):
        beer = createBeerFromCursorInfos(self.beerRepository.get(beer_id))
        beer.pictureURL = self.beerRepository.getBeerURLFromStyleId(
            beer.type_id)[0]
        return beer

    def getAll(self):
        repoBeers = self.beerRepository.getAll()
        beers = [createBeerFromCursorInfos(beer) for beer in repoBeers]
        print(beers)
        return beers

if __name__ == '__main__':
    beerRepo = BeerService()
    beerRepo.getAll()
