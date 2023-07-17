from button import *
import pygame

fonts = font_init()
rect_setting = pygame.Rect(325, 50, 375, 400)
up_rect_setting = pygame.Rect(310, 35, 405, 15)
down_rect_setting = pygame.Rect(310, 450, 405, 15)

button_background = Button(615, 75, fonts["georgia"], "BACKGROUND", COLOR_GREEN)
button_enemy = Button(555, 150, fonts["georgia"], "ENEMY", COLOR_GREEN)
button_item = Button(545, 250, fonts["georgia"], "ITEM", COLOR_GREEN)
button_sound = Button(565, 350, fonts["georgia"], "SOUND")

scroll_background = 0
scroll_enemy = 0
scroll_item = 0

play_sound = False


def setting():
    global scroll_background, scroll_enemy, scroll_item, button_sound, play_sound

    running = True
    mouse_pos = pygame.mouse.get_pos()
    if not rect_setting.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            running = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
    # Draw own rect
    pygame.draw.rect(screen, COLOR_GREEN_OFF_COLLIDE_BUTTON, up_rect_setting)
    pygame.draw.rect(screen, COLOR_GREEN_SETTING, rect_setting)
    pygame.draw.rect(screen, COLOR_GREEN_OFF_COLLIDE_BUTTON, down_rect_setting)
    # Scroll Background
    if button_background.draw(True):
        scroll_background = (scroll_background + 1) if scroll_background+1 < len(background_list) else 0
    # Scroll Enemy
    screen.blit(pygame.transform.scale(enemy_list[scroll_enemy], (75, 75)), (580, 125))
    if button_enemy.draw(True):
        scroll_enemy = (scroll_enemy + 1) if scroll_enemy+1 < len(enemy_list) else 0
    # Scroll Item
    screen.blit(pygame.transform.scale(item_list[scroll_item], (75, 75)), (580, 225))
    if button_item.draw(True):
        scroll_item = (scroll_item + 1) if scroll_item+1 < len(item_list) else 0
    # On / Off sound
    if button_sound.draw(True):
        play_sound = not play_sound
        latinophonic.play(loops=True) if play_sound else latinophonic.stop()

    return running, background_list[scroll_background], enemy_list[scroll_enemy], item_list[scroll_item]
