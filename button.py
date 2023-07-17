from setting import *
import pygame


class Button:
    def __init__(self, x: int, y: int, font: pygame.font.Font, text: str, color=COLOR_GREEN):
        self.color = color
        self.font = font
        self.str_text = text
        self.text = font.render(text, True, self.color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x-self.text.get_width(), y)
        self.click = False

    def draw(self, on_collide):
        self.text = self.font.render(self.str_text, True, self.color)
        screen.blit(self.text, (self.rect.x, self.rect.y))
        if on_collide:
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                pygame.draw.rect(screen, self.color, self.rect, 1)
                if pygame.mouse.get_pressed()[0] == 1 and not self.click:
                    self.click = True
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

            return action


class ButtonLevels:
    def __init__(self, x: int, y: int, width: int, height: int, font: pygame.font.Font, text: str, color=COLOR_GREEN):
        self.color = color
        self.font = font
        self.str_text = text
        self.text = font.render(text, True, COLOR_WHITE)
        self.rect = pygame.Rect(x, y, width, height)
        self.click = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, (self.rect.x+self.rect.width//2-10, self.rect.y+self.rect.height//2-20))
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, COLOR_BLACK, self.rect, 3)
            if pygame.mouse.get_pressed()[0] == 1 and not self.click:
                self.click = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        return action
