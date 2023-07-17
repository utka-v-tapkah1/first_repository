from setting import *

fonts = font_init()
y = 0
text_Gratitude = fonts["arial black"].render("Отдельная благодарность", True, COLOR_WHITE)
text_Developers = fonts["arial black"].render("Разработчики", True, COLOR_WHITE)
text_Producer = fonts["arial black"].render("Продюсер", True, COLOR_WHITE)
text_Screenwriters = fonts["arial black"].render("Сценаристы", True, COLOR_WHITE)
text_Designers = fonts["arial black"].render("Дизайнеры", True, COLOR_WHITE)
name_Valeria = fonts["arial"].render("Валера Вет", True, COLOR_WHITE)
name_Nikolay = fonts["arial"].render("Николай Багажов", True, COLOR_WHITE)
name_Magomed = fonts["arial"].render("Магомед Мирный", True, COLOR_WHITE)
name_Maksim = fonts["arial"].render("Максимилиан Последевятого", True, COLOR_WHITE)
name_Dimitry = fonts["arial"].render("Димитрий Духно", True, COLOR_WHITE)
name_Daniil = fonts["arial"].render("Даниил Флейта", True, COLOR_WHITE)
name_Artemy = fonts["arial"].render("Артемий Аверьянов", True, COLOR_WHITE)


def titles():
    global y
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        y = 0
        return False
    running = True
    screen.fill(COLOR_BLACK)
    # Developers
    screen.blit(text_Developers, (360, 200-y))
    screen.blit(name_Dimitry, (380, 260-y))
    # Producer
    screen.blit(text_Producer, (390, 360-y))
    screen.blit(name_Dimitry, (380, 420-y))
    # Screenwriters
    screen.blit(text_Screenwriters, (375, 520-y))
    screen.blit(name_Dimitry, (380, 580-y))
    # Designers
    screen.blit(text_Designers, (380, 680-y))
    # screen.blit(name_Daniil, (385, 740-y))
    screen.blit(name_Nikolay, (375, 740-y))
    screen.blit(name_Maksim, (320, 800-y))
    screen.blit(name_Magomed, (380, 860-y))
    screen.blit(name_Valeria, (410, 920-y))
    # Gratitude
    screen.blit(text_Gratitude, (290, 1020-y))
    screen.blit(name_Artemy, (375, 1080-y))
    if y == 1200:
        y = 0
        running = False
    y += 1
    return running
