class Lobby:
    def __init__(self, id_, name, players=None, players_needed=2, creator=None):
        self.id = id_
        self.name = name
        self.players = players
        self.players_needed = players_needed
        self.creator = creator
