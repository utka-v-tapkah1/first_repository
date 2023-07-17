import pygame.image

from setting import *

fonts = font_init()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tile_size):
        super().__init__()

        self.standart_speed = 5
        self.speed = self.standart_speed
        self.direction = pygame.math.Vector2(0, 0)
        self.on_ground = False
        self.gravity = 0.8
        self.jump_speed = -16
        self.score = 0
        self.last_score = 0
        self.text = fonts["arial"].render(f"YOU SCORE: {self.score}", True, COLOR_BLACK)

        self.player_right = [pygame.transform.scale(pygame.image.load(f"image/player_right/right{i}.png"), (tile_size, tile_size)) for i in range(1, 5)]
        self.player_left = [pygame.transform.scale(pygame.image.load(f"image/player_left/left{i}.png"), (tile_size, tile_size)) for i in range(1, 5)]
        self.animation_timer = 0
        self.turn = "right"
        self.image = self.player_right[0]

        self.rect = self.player_right[0].get_rect(topleft=pos)
        self.rect.height -= 4

        self.invincibility_duration = 500
        self.invincible = False
        self.hurt_time = 0
        self.side_collide_enemy = "right"

    def get_input(self):
        keys = pygame.key.get_pressed()

        if self.animation_timer+1 >= len(self.player_left):
            self.animation_timer = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.animation_timer += 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.animation_timer += 1
        else:
            self.direction.x = 0
            self.animation_timer = 0

        if keys[pygame.K_SPACE]:
            if self.on_ground:
                self.jump()

    def get_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def get_damage(self, side_collide: str):
        if not self.invincible:
            self.direction.y -= 12
            self.score -= 5
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
            self.side_collide_enemy = side_collide.lower()

    def invincibility_timer(self):
        if self.invincible:
            if self.side_collide_enemy == "right":
                self.direction.x = -1
            elif self.side_collide_enemy == "left":
                self.direction.x = 1
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.direction.x = 0
                self.invincible = False

    def check_lose(self):
        if self.score < 0 or self.rect.bottom >= HEIGHT:
            self.score = 0
            lose_sound.play()
            return "lose"
        else:
            return True

    def update(self):
        self.get_input()
        self.invincibility_timer()

        self.text = self.text = fonts["arial"].render(f"YOU SCORE: {self.score}", True, COLOR_BLACK)
        self.last_score = self.score
        if self.direction.x < 0:
            self.turn = "left"
        elif self.direction.x > 0:
            self.turn = "right"
        self.image = self.player_right[self.animation_timer] if self.turn == "right" else self.player_left[self.animation_timer]
