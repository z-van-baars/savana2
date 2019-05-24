import art
from entity import Entity


class Plant(Entity):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile)


class Tree(Plant):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile)
        self.image = art.plant_images["tree"]