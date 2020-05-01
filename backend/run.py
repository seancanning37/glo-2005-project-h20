from flask import Flask, render_template
from flask_cors import CORS
from blueprints import beers
from blueprints import home
from blueprints import signup
from blueprints import login
from blueprints import customers
from blueprints import brands
from initialisation_script import createDatabaseScript, runAllInitScript


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

app.secret_key = "complete_random_secret_key"

cors = CORS(app, resources={r"/*": {"origin": "*"}})


# Implementation from: https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
def registerRoutes():
    app.register_blueprint(home.home)
    app.register_blueprint(beers.beers)
    app.register_blueprint(signup.signup_blueprint)
    app.register_blueprint(login.login_blueprint)
    app.register_blueprint(customers.customers_blueprint)
    app.register_blueprint(brands.brands)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    createDatabaseScript('../database/db_init/create_database.sql')
    runAllInitScript()
    registerRoutes()
    app.run(debug='true')
