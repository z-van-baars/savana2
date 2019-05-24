from entity import Entity
from entity import Item


class Animal(Entity):
    def __init__(self, column, row, tile, eats):
        super().__init__(column, row, tile)
        self.sight = 5
        self.speed = 4
        self.eats = eats


class Gazelle(Animal):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile)


class Buffalo(Animal):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile)


class Cheetah(Animal):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile, [])


class Jackal(Animal):
    def __init__(self, column, row, tile):
        super().__init__(column, row, tile)
