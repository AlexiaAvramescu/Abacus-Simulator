import pygame
from Buttons import button

bila_im = pygame.image.load('rounded.png').convert_alpha()
visible_sprites_jap = pygame.sprite.Group()

x = 140
list_sus = []
for i in range(9):
    list = []
    y = 150
    for j in range(2):
        bila = button(x, y, bila_im)
        visible_sprites_jap.add(bila)
        if j == 1:
            bila.toggle_visibility()
        list.append(bila)
        y = y + 60
    x = x + 90
    list_sus.append(list)

list_jos = []
x = 140
for i in range(9):
    list = []
    y = 280
    for j in range(5):
        bila = button(x, y, bila_im)
        visible_sprites_jap.add(bila)
        if j == 0:
            bila.toggle_visibility()
        list.append(bila)
        y = y + 60
    x = x + 90
    list_jos.append(list)
