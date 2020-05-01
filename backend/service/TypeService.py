from domain.Type import Type
from persistence import TypeRepository


def createTypeFromCursorInfos(typeInfos):
    beerType = Type()
    beerType.id = typeInfos[0]
    beerType.name = typeInfos[1]
    return beerType


class TypeService:
    def __init__(self):
        self.typeRepository = TypeRepository.TypeRepository()

    def get(self, type_id):
        beerType = createTypeFromCursorInfos(
            self.typeRepository.get(type_id))
        return beerType
