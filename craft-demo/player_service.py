from flask import jsonify
import os.path
from os import path
import csv


class PlayerInfo:
    players = []
    player_map = {}

    def get_player_by_id(self, id):
        if id not in self.player_map:
            return None

        player = self.player_map[id]
        return player

    def get_all_players(self):
        return self.players


class Player:
    def __init__(self, input):
        self.player_id = input[0]
        self.birth_year = input[1]
        self.birth_month = input[2]
        self.birth_date = input[3]
        self.birth_country = input[4]
        self.birth_state = input[5]
        self.birth_city = input[6]
        self.death_year = input[7]
        self.death_month = input[8]
        self.death_day = input[9]
        self.death_country = input[10]
        self.death_state = input[11]
        self.death_city = input[12]
        self.name_first = input[13]
        self.name_last = input[14]
        self.name_given = input[15]
        self.weight = input[16]
        self.height = input[17]
        self.bats = input[18]
        self.throws = input[19]
        self.debut = input[20]
        self.final_game = input[21]
        self.retro_id = input[22]
        self.bbref_id = input[23]

    def to_json(self):
        player = {
                "player_id": self.player_id,
                "birth year": self.birth_year,
                "birth_month": self.birth_month,
                "birth_date": self.birth_date,
                "birth_country": self.birth_country
        }
        return player




    @staticmethod
    def read_from_file(file_name):
        p = PlayerInfo()
        if path.exists(file_name):
            with open(file_name, newline='') as csv_file:
                reader = csv.reader(csv_file)
                next(reader, None)  # Skip the header.
                # Unpack the row directly in the head of the for loop.
                for row in reader:
                    player = Player(row)
                    p.players.append(player)
                    p.player_map[player.player_id] = player

        print(p.players)

        return p


if __name__ == "__main__":
    Player.read_from_file("Player.csv")
