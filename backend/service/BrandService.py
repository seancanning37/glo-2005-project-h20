from domain.Brand import Brand
from persistence import BrandRepository
from service.BeerService import createBeerFromCursorInfos


def createBrandFromCursorInfos(brandInfos):
    brand = Brand()
    brand.id = brandInfos[0]
    brand.name = brandInfos[1]
    brand.phone = brandInfos[2]
    brand.address = brandInfos[3]
    brand.city = brandInfos[4]
    brand.country = brandInfos[5]
    return brand


class BrandService:
    def __init__(self):
        self.brandRepository = BrandRepository.BrandRepository()

    def get(self, brand_id):
        brand = createBrandFromCursorInfos(self.brandRepository.get(brand_id))
        return brand

    def getAllBeers(self, brand_id):
        repoBeers = self.brandRepository.getAllBeers(brand_id)
        beers = [createBeerFromCursorInfos(
            beer) for beer in repoBeers]
        return beers

    def getAllBrands(self):
        return [createBrandFromCursorInfos(brand) for brand in self.brandRepository.getAllBrands()]
