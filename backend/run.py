from flask import Flask, render_template
from flask_cors import CORS
from routes import beers
from routes import home
from routes import signup
from routes import login
from initialisation_script import createDatabaseScript, runAllInitScript


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

cors = CORS(app, resources={r"/*": {"origin": "*"}})


def registerRoutes():
    app.register_blueprint(home.home)
    app.register_blueprint(beers.beers)
    app.register_blueprint(signup.signup_blueprint)
    app.register_blueprint(login.login_blueprint)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    createDatabaseScript('../database/db_init/create_database.sql')
    runAllInitScript()
    registerRoutes()
    app.run()
