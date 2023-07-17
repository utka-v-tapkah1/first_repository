from menu_setting import *
from titles import titles
from menu_levels import menu_levels
from game_menu import game_menu
from map import *
from maps import *
from menu_lose import menu_lose
from menu_win import menu_win
import pygame
pygame.init()

fonts = font_init()

score = 0

button_start = Button(WIDTH-10, 200, fonts["georgia"], "START", COLOR_GREEN)
button_setting = Button(WIDTH-10, 235, fonts["georgia"], "SETTING", COLOR_GREEN)
button_titles = Button(WIDTH-10, 270, fonts["georgia"], "TITLES", COLOR_GREEN)
button_exit = Button(WIDTH-10, 305, fonts["georgia"], "EXIT", COLOR_GREEN)

buttons = (button_start, button_setting, button_titles, button_exit)

background = background_list[scroll_background]

enemy = enemy_list[0]
item = item_list[0]

level_one = Map(level_one_map, enemy, item)
level_two = Map(level_two_map, enemy, item)
level_three = Map(level_one_map, enemy, item)


def event_checker():
    global running, run_standart_menu, run_setting, run_game, run_game_menu, run_levels_menu, lose_menu, win_menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and run_game and not (lose_menu or win_menu):
                run_game_menu = not run_game_menu
            if event.key == pygame.K_ESCAPE and run_levels_menu:
                run_levels_menu = False
                run_standart_menu = True


run_game = False
run_game_menu = False
levels_play = [False, False, False]
levels = [level_one, level_two, level_three]
level_maps = [level_one_map, level_two_map, level_three_map]
level_playing = 0

run_setting = False
run_titles = False
run_standart_menu = True
run_levels_menu = False

lose_menu = False
win_menu = False

running = True

if __name__ == "__main__":
    while running:
        screen.blit(background, (0, 0))
        event_checker()

        # Start Menu
        if run_standart_menu:
            # Setting
            if run_setting:
                for button in buttons:
                    if button != button_setting:
                        button.color = COLOR_GREEN_OFF_COLLIDE_BUTTON
                    button.draw(False)
                run_setting, background, enemy, item = setting()
                if not run_setting:
                    clock.tick(10)
            # Titles
            elif run_titles:
                run_titles = titles()
            # Menu
            else:
                for button in buttons:
                    button.color = COLOR_GREEN
                # Start
                if button_start.draw(True):
                    run_standart_menu = False
                    run_levels_menu = True
                    clock.tick(10)
                # Setting
                elif button_setting.draw(True):
                    run_setting = True
                    clock.tick(10)
                # Titles
                elif button_titles.draw(True):
                    run_titles = True
                    clock.tick(10)
                # Exit
                elif button_exit.draw(True):
                    running = False
        # Menu all levels
        elif run_levels_menu:
            run_levels_menu, run_game, run_game_menu, levels_play = menu_levels()
            if not run_levels_menu and not run_game:
                run_standart_menu = True
            if run_game:
                level_one.setup_level(level_one_map, enemy, item)
                level_two.setup_level(level_two_map, enemy, item)
                level_three.setup_level(level_three_map, enemy, item)
        # Run game
        elif run_game:
            # Game menu
            if run_game_menu:
                run_game, run_game_menu, restart = game_menu()
                if not run_game:
                    run_levels_menu = True
                if restart:
                    run_game_menu = False
                    levels[level_playing].setup_level(level_maps[level_playing], enemy, item)
            # Lose menu
            elif lose_menu:
                run_game, lose_menu = menu_lose(score)
                if not run_game:
                    lose_menu = False
                    run_levels_menu = True
                if not lose_menu:
                    levels_play[level_playing] = True
                    levels[level_playing].setup_level(level_maps[level_playing], enemy, item)
            # Win menu
            elif win_menu:
                run_game, win_menu = menu_win(score)
                if not run_game:
                    win_menu = False
                    run_levels_menu = True
                if not win_menu:
                    levels_play[level_playing] = True
                    levels[level_playing].setup_level(level_maps[level_playing], enemy, item)
            # Run level one
            elif levels_play[0]:
                levels_play[0], score = level_one.run()
                level_playing = 0
            # Run level two
            elif levels_play[1]:
                levels_play[1], score = level_two.run()
                level_playing = 1
            # Run level three
            elif levels_play[2]:
                levels_play[2], score = level_three.run()
                level_playing = 2
            # Check lose or win
            if levels_play[level_playing] == "lose":
                lose_menu = True
            elif levels_play[level_playing] == "win":
                win_menu = True

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()
