import pygame
import art
import state
import game_map
import utilities as util
import plant

pygame.init()
pygame.display.set_mode([800, 600])


def do_nothing(game_state, mouse_pos=(0, 0), map_xy=(0, 0), *button_states):
    pass


def up_key(game_state):
    game_state.active_map.world_scroll(0,
                                       40,
                                       game_state.screen_width,
                                       game_state.screen_height)


def down_key(game_state):
    game_state.active_map.world_scroll(0,
                                       -40,
                                       game_state.screen_width,
                                       game_state.screen_height)


def left_key(game_state):
    game_state.active_map.world_scroll(40,
                                       0,
                                       game_state.screen_width,
                                       game_state.screen_height)


def right_key(game_state):
    game_state.active_map.world_scroll(-40,
                                       0,
                                       game_state.screen_width,
                                       game_state.screen_height)


def left_click(game_state, mouse_pos, map_xy, button_states, event):
    game_state.active_map.plant


def scrollwheel_click(game_state, mouse_pos, map_xy, button_states, event):
    pass


def right_click(game_state, mouse_pos, map_xy, button_states, event):
    pass


key_functions = {pygame.K_UP: up_key,
                 pygame.K_DOWN: down_key,
                 pygame.K_LEFT: left_key,
                 pygame.K_RIGHT: right_key}

mouseclick_functions = {(1, 0, 0): left_click,
                        (0, 1, 0): scrollwheel_click,
                        (0, 0, 1): right_click}


def event_handler(game_state, pos, map_xy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_1, button_2, button_3 = pygame.mouse.get_pressed()
            button_states = (button_1, button_2, button_3)
            mouseclick_functions.get(button_states, do_nothing)(
                game_state,
                pos,
                map_xy,
                button_states,
                event)
        elif event.type == pygame.MOUSEBUTTONUP:
            button_1, button_2, button_3 = pygame.mouse.get_pressed()
            button_states = (button_1, button_2, button_3)
            left_click(
                game_state,
                pos,
                map_xy,
                button_states,
                event)
        elif event.type == pygame.KEYDOWN:
            key_functions.get(event.key, do_nothing)(game_state)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                game_state.control = False


def display_update(game_state, selected_tile, pos, map_xy):
    active_map = game_state.active_map
    screen = game_state.screen
    game_state.screen.fill(util.colors.background_blue)
    tile_width = 40

    game_state.screen.blit(
        active_map.tile_display_layer.image,
        [game_state.background_left, game_state.background_top])

    for plant in active_map.plants:
        # converts the player's x, y tile to pixel coordinates
        plant_pixel_coordinates = util.get_screen_coords(plant.column, plant.row)
        # offsets the true pixel coordinates by the current display shift
        plant_screen_coordinates = (plant_pixel_coordinates[0] + game_state.background_x_middle + (tile_width / 2),
                                     plant_pixel_coordinates[1] + game_state.background_top)
        # 20 and 25 are graphical offsets - x and y - so that the player's ship image is centered on the tile
        screen.blit(plant.image, [plant_screen_coordinates[0] - 20,
                                  plant_screen_coordinates[1] - 25])
    for animal in active_map.animals:
        pass

    if selected_tile:
        st_pixel_coordinates = util.get_screen_coords(map_xy[0], map_xy[1])
        st_screen_coordinates = st_pixel_coordinates[0] + game_state.background_x_middle + (tile_width / 2) - 20, st_pixel_coordinates[1] + game_state.background_top
        screen.blit(
            art.selected_tile_image,
            [st_screen_coordinates[0], st_screen_coordinates[1]])


    pygame.display.flip()


screen_width = 800
screen_height = 600
game_state = state.GameState(screen_width, screen_height)
game_state.active_map = game_map.Map([25, 25], [screen_width, screen_height])
game_state.active_map.mapgen()
new_tree = plant.Tree(0, 0, game_state.active_map.game_tile_rows[0][0])
game_state.active_map.plants.append(new_tree)


def main():
    active_map = game_state.active_map
    active_map.x_shift = game_state.screen_width / 2 - (game_state.background_width / 2)
    active_map.y_shift = game_state.screen_height / 2 - (game_state.background_height / 2)
    while True:
        pos = pygame.mouse.get_pos()
        map_xy = util.get_map_coords(pos,
                                     game_state.active_map.x_shift,
                                     game_state.active_map.y_shift,
                                     game_state.background_x_middle)
        selected_tile = None
        if util.check_if_inside(0, active_map.width, 0, active_map.height, map_xy):
            selected_tile = active_map.game_tile_rows[map_xy[1]][map_xy[0]]
        event_handler(game_state, pos, map_xy)
        display_update(game_state, selected_tile, pos, map_xy)

main()