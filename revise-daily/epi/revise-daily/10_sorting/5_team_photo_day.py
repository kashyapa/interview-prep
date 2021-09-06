from collections import namedtuple


class Team:
    Player = namedtuple('Player', 'height')

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]


#
    @staticmethod
    def valid_placement_exists(team0: 'Team', team1: 'Team'):
        return all(
            a < b for a, b in zip(sorted(team0._players), sorted(team1._players))
        )



