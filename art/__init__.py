import pygame
import utilities


pygame.init()
pygame.display.set_mode([800, 600])

key_color = utilities.colors.key


selected_tile_image = pygame.image.load("art/tiles/selected_tile.png").convert_alpha()
selected_tile_image.set_colorkey(utilities.colors.key)
selected_tile_image = selected_tile_image.convert_alpha()
grass_tile = pygame.image.load("art/tiles/grassland_1.png").convert_alpha()
grass_tile.set_colorkey(utilities.colors.key)
grass_tile = grass_tile.convert_alpha()
tree_image = pygame.image.load("art/terrain/tree_1.png").convert_alpha()
tree_image.set_colorkey(utilities.colors.key)
tree_image = tree_image.convert_alpha()

plant_images = {"tree": tree_image}
biome_images = {
    "grass": [grass_tile]}
