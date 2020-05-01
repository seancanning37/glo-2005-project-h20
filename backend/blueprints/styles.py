from flask import Blueprint, jsonify

from service.StyleService import StyleService

styles = Blueprint("styles", __name__, url_prefix="/")


@styles.route("styles/<style_id>", methods=['GET'])
def getStyle(style_id):
    styleservice = StyleService()
    style = styleservice.get(style_id)
    return jsonify(style.__dict__)
