import pygame
from Buttons import button_meniu
from Buttons import buttons_abac
from Buttons import button_exit
from Buttons import button_refresh
font_esc=pygame.font.SysFont('timesnewroman',15,True)
meniu=True
meniu_im=pygame.image.load('rounded.png')
meniu_esc=button_meniu(45,45,meniu_im)
meniu_txt="Meniu"

font_meniu=pygame.font.SysFont('timesnewroman',45,True)
Chi_but_cond=False
Chi_im=pygame.image.load('Buton meniu.png')
Chi_but=buttons_abac(500,440,Chi_im)
Chi_txt_sus="Abac"
Chi_txt_jos="Chinzesc"

Jap_but_cond=False
Jap_txt_sus="Abac"
Jap_txt_jos="Japonez"
Jap_im=pygame.image.load('Buton meniu.png')
Jap_but=buttons_abac(500,270,Jap_im)

font_exit=pygame.font.SysFont('timesnewroman',24,True)
exit_txt="EXIT"
exit_im=pygame.image.load('exit.png')
exit_but=button_exit(500,530,exit_im)

font_esc=pygame.font.SysFont('timesnewroman',16,True)
refresh_im=pygame.image.load('rounded.png')
refresh_but=button_refresh(499,45,refresh_im)
refresh_txt="Refresh"