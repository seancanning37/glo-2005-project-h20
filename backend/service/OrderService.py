from domain.Order import Order
from persistence import OrderRepository

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


class OrderService:
    def __init__(self):
        self.OrderRepository = OrderRepository.OrderRepository()

    def get(self, order_id):
        return
