from button import *

fonts = font_init()

button_start = Button(WIDTH-10, 235, fonts["georgia"], "RESTART", COLOR_GREEN)
button_exit = Button(WIDTH-10, 270, fonts["georgia"], "EXIT", COLOR_GREEN)


def menu_win(score):
    screen.blit(fonts["big arial"].render(f"WIN", True, COLOR_BLACK), (435, 350))
    screen.blit(fonts["big arial"].render(f"YOU SCORE: {score}", True, COLOR_BLACK), (325, 450))

    running = True
    running_menu = True
    # Start
    if button_start.draw(True):
        running_menu = False
        clock.tick(10)
    # Exit
    elif button_exit.draw(True):
        running = False

    return running, running_menu
