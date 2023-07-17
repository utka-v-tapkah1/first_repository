from button import *

fonts = font_init()

button_start = Button(WIDTH-10, 235, fonts["georgia"], "CONTINUE", COLOR_GREEN)
button_restart = Button(WIDTH-10, 270, fonts["georgia"], "RESTART", COLOR_GREEN)
button_exit = Button(WIDTH-10, 305, fonts["georgia"], "EXIT", COLOR_GREEN)


def game_menu():
    running = True
    running_menu = True
    restart = False
    # Start
    if button_start.draw(True):
        running_menu = False
        clock.tick(10)
    elif button_restart.draw(True):
        restart = True
    # Exit
    elif button_exit.draw(True):
        running = False

    return running, running_menu, restart
