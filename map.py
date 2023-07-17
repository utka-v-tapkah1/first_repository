import random

from setting import *
from tile import *
from player import Player


class Map:
    tiles: pygame.sprite.Group
    enemies: pygame.sprite.Group
    coins: pygame.sprite.Group
    exits: pygame.sprite.Group
    player: pygame.sprite.GroupSingle
    enemy: pygame.sprite.Sprite
    item: pygame.sprite.Sprite
    text: pygame.Surface
    tile_size: int
    count_timer: int

    def __init__(self, level_data, enemy, item):
        self.setup_level(level_data, enemy, item)
        self.world_shift = 0

    def setup_level(self, level_data, enemy, item):
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.tile_size = HEIGHT // len(level_data)
        self.player = pygame.sprite.GroupSingle()
        self.enemy = enemy
        self.item = item
        self.count_timer = 0

        for row_index, row in enumerate(level_data):
            for col_index, col in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if col == 'G':
                    grass_tile = Tile((x, y), grass, self.tile_size)
                    self.tiles.add(grass_tile)
                if col == 'D':
                    dirt_tile = Tile((x, y), dirt, self.tile_size)
                    self.tiles.add(dirt_tile)
                if col == 'E':
                    enemy_tile = Tile((x, y), self.enemy, self.tile_size, 1)
                    self.enemies.add(enemy_tile)
                if col == 'C':
                    coin_tile = Tile((x+10, y+10), self.item, self.tile_size//2)
                    self.coins.add(coin_tile)
                if col == 'P':
                    player_sprite = Player((x, y), self.tile_size)
                    self.player.add(player_sprite)
                if col == 'X':
                    exit_tile = Tile((x+2.5, y+5), pygame.Surface((1, 1)), 50, 50)
                    self.exits.add(exit_tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH / 4 and direction_x < 0:
            self.world_shift = player.standart_speed
            player.speed = 0
        elif player_x > WIDTH - WIDTH / 4 and direction_x > 0:
            self.world_shift = -player.standart_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player.standart_speed

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.get_gravity()

        player.on_ground = False
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                    player.on_ground = True

    def check_collide_enemy(self):
        collided_enemy = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)
        player = self.player.sprite

        if collided_enemy:
            for enemy in collided_enemy:
                player_bottom = player.rect.bottom
                if enemy.rect.top < player_bottom < enemy.rect.centery and self.player.sprite.direction.y >= 0:
                    self.enemies.remove(enemy)
                    player.score += 1
                    player.direction.y = -12
                    kill_enemy_sound.play()
                else:
                    if player.rect.right < enemy.rect.right:
                        player.get_damage("right")
                    else:
                        player.get_damage("left")
                    if player.score >= 0:
                        collide_enemy_sound.play()
                    self.count_timer = 0

    def check_collide_coin(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite, self.coins, True)
        if collided_coins:
            for _ in collided_coins:
                self.player.sprite.score += 1
                collide_coin_sound.play()

    def check_exit(self):
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.exits, False):
            win_sound.play()
            return True

    def run(self):
        screen.blit(self.player.sprite.text, (0, 0))

        self.tiles.update(self.world_shift)
        self.tiles.draw(screen)

        self.enemies.update(self.world_shift)
        self.enemies.draw(screen)

        self.coins.update(self.world_shift)
        self.coins.draw(screen)

        self.exits.update(self.world_shift)
        self.exits.draw(screen)

        self.scroll_x()

        self.player.update()

        if not self.player.sprite.invincible:
            self.check_collide_coin()
            self.check_collide_enemy()
        else:
            player = self.player.sprite
            if random.randint(1, 3) and self.count_timer < 5:
                tile = Tile((player.rect.centerx+(self.count_timer*10)*player.direction.x, player.rect.top-20), self.item, self.tile_size//2)
                tile.update(random.randint(-1, 1) * 8)
                self.coins.add(tile)
                self.count_timer += 1

        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(screen)

        if self.check_exit():
            return "win", self.player.sprite.last_score
        return self.player.sprite.check_lose(), self.player.sprite.last_score
