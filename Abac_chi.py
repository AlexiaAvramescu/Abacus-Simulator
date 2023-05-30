import pygame
from Buttons import button

bila_im = pygame.image.load('rounded.png').convert_alpha()
visible_sprites_chi = pygame.sprite.Group()

x = 140
list_sus_chi = []
for i in range(9):
    list = []
    y = 120
    for j in range(3):
        bila = button(x, y, bila_im)
        visible_sprites_chi.add(bila)
        if j == 2:
            bila.toggle_visibility()
        list.append(bila)
        y = y + 60
    x = x + 90
    list_sus_chi.append(list)

list_jos_chi = []
x = 140
for i in range(9):
    list = []
    y = 310
    for j in range(6):
        bila = button(x, y, bila_im)
        visible_sprites_chi.add(bila)
        if j == 0:
            bila.toggle_visibility()
        list.append(bila)
        y = y + 60
    x = x + 90
    list_jos_chi.append(list)
