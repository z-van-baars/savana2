

class GameTile(object):
    def __init__(self, column, row, biome):
        self.column = column  # X
        self.row = row  # Y
        self.biome = biome
        self.terrain = None

    def __lt__(self, other):
        return False

