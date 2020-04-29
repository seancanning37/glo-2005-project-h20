from flask import Blueprint, jsonify

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def main():
    return "hello world"
