import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image, tile_size, plus_tile_size_y=0):
        super().__init__()
        self.image = pygame.transform.scale(image, (tile_size, tile_size + plus_tile_size_y))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1]-plus_tile_size_y))

    def update(self, x):
        self.rect.x += x
