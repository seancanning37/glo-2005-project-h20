from flask import Flask
from flask_cors import CORS
from backend.initialisation_script import createDatabaseScript, runAllInitScript
from backend.routes.beers import beers
from backend.routes.home import home


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

cors = CORS(app, resources={r"/*": {"origin": "*"}})


def registerRoutes():
    app.register_blueprint(home)
    app.register_blueprint(beers)


"""
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
"""
if __name__ == "__main__":
    createDatabaseScript('database/db_init/create_database.sql')
    runAllInitScript()
    registerRoutes()
    app.run()
