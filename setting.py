import pygame
from pygame.font import SysFont


def font_init():
    pygame.font.init()
    return {
        "georgia": SysFont("georgia", 26, True),
        "arial": SysFont("arial", 26, True),
        "arial black": SysFont("arial black", 26, True),
        "small arial": SysFont("arial", 13, True),
        "big arial": SysFont("arial", 52, True)
    }


WIDTH = 900
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("UltraMegaGame")

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (100, 100, 200)
COLOR_RED = (200, 100, 100)
COLOR_GREEN = (110, 200, 110)
COLOR_GREEN_SETTING = pygame.color.Color(0, 50, 0, 125)
COLOR_GREEN_OFF_COLLIDE_BUTTON = (50, 100, 50)


background_list = (
    pygame.transform.scale(pygame.image.load("image/KolyaTheme/Background.png"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("image/LeraTheme/Background.jpg"), (WIDTH, HEIGHT))
)
enemy_list = (
    pygame.image.load("image/KolyaTheme/Enemy.png"),
    pygame.image.load("image/MagaTheme/Enemy.png"),
    pygame.image.load("image/MaksimTheme/Enemy.png")
)
item_list = (
    pygame.image.load("image/KolyaTheme/Item.png"),
    pygame.image.load("image/MaksimTheme/Item.png")
)
dirt = pygame.image.load("image/KolyaTheme/Dirt.png")
grass = pygame.image.load("image/KolyaTheme/Grass.png")

pygame.mixer.init()
kill_enemy_sound = pygame.mixer.Sound("sound/kill_enemy.mp3")
collide_enemy_sound = pygame.mixer.Sound("sound/collide_enemy.mp3")
collide_coin_sound = pygame.mixer.Sound("sound/collide_coin.mp3")
lose_sound = pygame.mixer.Sound("sound/lose.mp3")
win_sound = pygame.mixer.Sound("sound/win.mp3")
latinophonic = pygame.mixer.Sound("sound/Latinophonic.mp3")
