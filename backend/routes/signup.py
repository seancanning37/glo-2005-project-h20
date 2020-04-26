from flask import Blueprint, jsonify

signup_blueprint = Blueprint("signup", __name__, url_prefix="/")


@signup_blueprint.route("signup", methods=['POST'])
def signup():
    print("Je me rend ici")
    return jsonify({"key": "value"})
