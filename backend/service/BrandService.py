from domain.Brand import Brand
from persistence import BrandRepository


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
