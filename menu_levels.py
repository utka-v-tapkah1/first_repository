from button import *
from maps import *
import pygame

fonts = font_init()

max_score_level_one = sum(row.count('C') + row.count('E') for row in level_one_map)
max_score_level_two = sum(row.count('C') + row.count('E') for row in level_two_map)
max_score_level_three = sum(row.count('C') + row.count('E') for row in level_three_map)

level_one = ButtonLevels(75, 200, 150, 150, fonts["arial black"], "1", COLOR_BLUE)
level_two = ButtonLevels(375, 200, 150, 150, fonts["arial black"], "2", COLOR_BLUE)
level_three = ButtonLevels(675, 200, 150, 150, fonts["arial black"], "3", COLOR_BLUE)

arrow_rect = pygame.Rect(WIDTH-103, 18, 95, 35)

levels = [False, False, False]
click = False


def menu_levels():
    global click, levels
    running = True
    run_game = False
    mouse_pos = pygame.mouse.get_pos()
    color = COLOR_GREEN
    # Draw exit arrow
    if arrow_rect.collidepoint(mouse_pos):
        color = COLOR_BLACK
        if pygame.mouse.get_pressed()[0] == 1 and not click:
            running = False
    pygame.draw.lines(screen, color, True, (
        (WIDTH - 100, 30),
        (WIDTH - 40, 30),
        (WIDTH - 50, 20),
        (WIDTH - 35, 20),
        (WIDTH - 10, 35),
        (WIDTH - 35, 50),
        (WIDTH - 50, 50),
        (WIDTH - 40, 40),
        (WIDTH - 100, 40)
    ), 5)
    # Check click on button levels
    if level_one.draw():
        levels = [True, False, False]
        run_game = True
        running = False
    screen.blit(fonts["small arial"].render(f"Max score: {max_score_level_one}", True, COLOR_BLACK),
                (level_one.rect.left + level_one.rect.width//3.5, level_one.rect.top+10))
    if level_two.draw():
        levels = [False, True, False]
        run_game = True
        running = False
    screen.blit(fonts["small arial"].render(f"Max score: {max_score_level_two}", True, COLOR_BLACK),
                (level_two.rect.left + level_two.rect.width // 3.5, level_two.rect.top + 10))
    if level_three.draw():
        levels = [False, False, True]
        run_game = True
        running = False
    screen.blit(fonts["small arial"].render(f"Max score: {max_score_level_three}", True, COLOR_BLACK),
                (level_three.rect.left + level_three.rect.width // 3.5, level_three.rect.top + 10))
    return running, run_game, False, levels
