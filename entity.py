


class Entity(object):
    def __init__(self, column, row, tile):
        self.column = column
        self.row = row
        self.tile = tile

    def change_tile(self, tile):
        self.column = tile.column
        self.row = tile.column
        self.tile = tile
