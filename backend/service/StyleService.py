from domain.Style import Style
from persistence import StyleRepository


def createStyleFromCursorInfos(styleInfos):
    style = Style()
    style.id = styleInfos[0]
    style.name = styleInfos[1]
    return style


class StyleService:
    def __init__(self):
        self.styleRepository = StyleRepository.StyleRepository()

    def get(self, style_id):
        style = createStyleFromCursorInfos(self.styleRepository.get(style_id))
        return style
