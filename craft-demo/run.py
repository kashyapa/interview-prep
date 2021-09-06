from src import app, api
from player_service import *
import json
from flask import jsonify

player_obj = []





def set_players_resource(p):
    player_obj.append(p)


def get_player_resource():
    return player_obj[0]

@app.route("/")
def homepage():
    """View function for Home Page."""

    return "Hello world!"


@app.route("/api/players")
def get_players():
    """View function for Home Page."""
    p = get_player_resource()
    all_players = p.get_all_players()
    if len(all_players) == 0:
        return jsonify(error="")
    all_players = [player.to_json() for player in all_players]
    return jsonify(all_players)


@app.route("/api/players/<player_id>")
def get_player(player_id):
    """View function for About Page."""
    p = get_player_resource()
    player = p.get_player_by_id(player_id)
    if player:
        return jsonify(player=player.to_json()), 201
    return jsonify(error="not found"), 404


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    p = Player.read_from_file(file_name)
    set_players_resource(p)
    app.run(debug=True, host="0.0.0.0", port=3000)

# optimize retrieval
# make the output return a json
