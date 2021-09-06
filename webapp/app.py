from src import app
from models import *
import json
from flask import request

@app.route("/")
def homepage():
    """View function for Home Page."""
    pets = Pet.query.all()
    res = [pet.name for pet in pets]
    return json.dumps(res)


@app.route("/about")
def about():
    """View function for About Page."""
    return json.dumps(request)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
