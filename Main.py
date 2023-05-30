import pygame

from Buttons import *
from Abac_jap import *
from Meniu import *
from Abac_chi import *

frame_color = (97, 97, 97)

def draw_frame():
    pygame.draw.line(screen, frame_color, (100, 85), (900, 85), 10)
    pygame.draw.line(screen, frame_color, (100, 217), (900, 217), 10)
    pygame.draw.line(screen, frame_color, (100, 530), (900, 530), 10)
    x = 140
    y_start = 85
    y_stop = 530
    for i in range(9):
        pygame.draw.line(screen, frame_color, (x, y_start), (x, y_stop), 5)
        x += 90
    pygame.draw.circle(screen, ('white'), (770, 218), 5)
    pygame.draw.circle(screen, ('white'), (500, 218), 5)
    pygame.draw.circle(screen, ('white'), (230, 218), 5)

def draw_frame_chi():
    pygame.draw.line(screen, frame_color, (100, 55), (900, 55), 10)
    pygame.draw.line(screen, frame_color, (100, 247), (900, 247), 10)
    pygame.draw.line(screen, frame_color, (100, 620), (900, 620), 10)
    x = 140
    y_start = 55
    y_stop = 620
    for i in range(9):
        pygame.draw.line(screen, frame_color, (x, y_start), (x, y_stop), 5)
        x += 90


font = pygame.font.Font(None, 45)
num_color = ('black')
list_num_jap = [0, 0, 0, 0, 0, 0, 0, 0, 0]
list_num_chi = [0, 0, 0, 0, 0, 0, 0, 0, 0]
clock = pygame.time.Clock()
running = True
while running:
    if meniu == False and Jap_but_cond == True:

        screen.fill(screen_color)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             pos = pygame.mouse.get_pos()
             if meniu_esc.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                 meniu = True
                 Jap_but_cond=False
                 Chi_but_cond=False

             for i in range(9):
                for j in range(2):
                    if list_sus[i][j].rect.collidepoint(pos) and list_sus[i][
                        j].visible == True and event.type == pygame.MOUSEBUTTONDOWN:
                        for x in range(2):
                            if x != j:
                                list_sus[i][x].visible = True
                        list_sus[i][j].toggle_visibility()
             for i in range(9):
                for j in range(5):
                    if list_jos[i][j].rect.collidepoint(pos) and list_jos[i][
                        j].visible == True and event.type == pygame.MOUSEBUTTONDOWN:
                        for x in range(5):
                            if x != j:
                                list_jos[i][x].visible = True
                        list_jos[i][j].toggle_visibility()
             if refresh_but.rect.collidepoint(pos) and event.type==pygame.MOUSEBUTTONDOWN:
                 for i in range (9):
                     for j in range(5):
                         if j==0:
                             list_jos[i][j].visible=False
                         else:
                             list_jos[i][j].visible=True
                 for i in range(9):
                     for j in range (2):
                         if j==1:
                             list_sus[i][j].visible=False
                         else:
                             list_sus[i][j].visible=True
        meniu_esc.draw()
        menu_draw = font_esc.render(meniu_txt, True, num_color)
        refresh_but.draw()
        screen.blit(menu_draw, (24, 21))

        refresh_but.draw()
        refresh_draw = font_esc.render(refresh_txt, True, num_color)
        screen.blit(refresh_draw, (473, 16))

        for i in range(9):
            for j in range(5):
                if list_jos[i][j].visible == False:
                    list_num_jap[i] = j

            for j in range(2):
                if list_sus[i][j].visible == True:
                    list_num_jap[i] += 5 * j

        visible_sprites_jap.update()
        draw_frame()

        x = 133
        y = 540
        for I in range(9):
            num_text = font.render(str(list_num_jap[I]), True, num_color)
            screen.blit(num_text, (x, y))
            x += 90
        for i in range(9):
            for j in range(2):
                if list_sus[i][j].visible == True:
                    list_sus[i][j].draw()
        for i in range(9):
            for j in range(5):
                if list_jos[i][j].visible == True:
                    list_jos[i][j].draw()

        pygame.display.update()
        clock.tick(60)


    elif meniu==True:

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             pos=pygame.mouse.get_pos()
             if Jap_but.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                Jap_but_cond=True
                meniu=False
             elif Chi_but.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                 Chi_but_cond = True
                 meniu = False
             elif exit_but.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                 running=False
        screen.fill(screen_color)
        Jap_but.draw()
        Chi_but.draw()

        Jap_txt_sus_draw=font_meniu.render(Jap_txt_sus, True, num_color)
        screen.blit(Jap_txt_sus_draw,(445,140))
        Jap_txt_jos_draw=font_meniu.render(Jap_txt_jos, True, num_color)
        screen.blit(Jap_txt_jos_draw,(415,185))

        Chi_txt_sus_draw = font_meniu.render(Chi_txt_sus, True, num_color)
        screen.blit(Chi_txt_sus_draw, (445, 310))
        Chi_txt_jos_draw = font_meniu.render(Chi_txt_jos, True, num_color)
        screen.blit(Chi_txt_jos_draw, (415, 355))

        exit_but.draw()
        exit_draw = font_exit.render(exit_txt, True, 'white')
        screen.blit(exit_draw, (471, 490))

        pygame.display.update()
        clock.tick(60)

    elif meniu==False and Chi_but_cond==True:
        screen.fill(screen_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pos=pygame.mouse.get_pos()
            if meniu_esc.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                meniu = True
                Jap_but_cond = False
                Chi_but_cond = False

            for i in range(9):
                for j in range(3):
                    if list_sus_chi[i][j].rect.collidepoint(pos) and list_sus_chi[i][
                        j].visible == True and event.type == pygame.MOUSEBUTTONDOWN:
                        for x in range(3):
                            if x != j:
                                list_sus_chi[i][x].visible = True
                        list_sus_chi[i][j].toggle_visibility()
            for i in range(9):
                for j in range(6):
                    if list_jos_chi[i][j].rect.collidepoint(pos) and list_jos_chi[i][
                        j].visible == True and event.type == pygame.MOUSEBUTTONDOWN:
                        for x in range(6):
                            if x!=j:
                                list_jos_chi[i][x].visible = True
                        list_jos_chi[i][j].toggle_visibility()
            if refresh_but.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(9):
                    for j in range(6):
                        if j == 0:
                            list_jos_chi[i][j].visible = False
                        else:
                            list_jos_chi[i][j].visible = True
                for i in range(9):
                    for j in range(3):
                        if j == 2:
                            list_sus_chi[i][j].visible = False
                        else:
                            list_sus_chi[i][j].visible = True
        draw_frame_chi()
        meniu_esc.draw()
        menu_draw = font_esc.render(meniu_txt, True, num_color)
        screen.blit(menu_draw, (24, 21))

        refresh_but.draw()
        refresh_draw=font_esc.render(refresh_txt,True,num_color)
        screen.blit(refresh_draw,(473,16))

        for i in range(9):
            for j in range(6):
                if list_jos_chi[i][j].visible == False:
                    list_num_chi[i] = j

            for j in range(3):
                if list_sus_chi[i][j].visible == False:
                    list_num_chi[i] +=  (2-j)*5

        visible_sprites_chi.update()
        x = 133
        y = 630
        for I in range(9):
            num_text = font.render(str(list_num_chi[I]), True, num_color)
            screen.blit(num_text, (x, y))
            x += 90
        for i in range(9):
            for j in range(3):
                if list_sus_chi[i][j].visible == True:
                    list_sus_chi[i][j].draw()
        for i in range(9):
            for j in range(6):
                if list_jos_chi[i][j].visible == True:
                    list_jos_chi[i][j].draw()

        pygame.display.update()
        clock.tick(60)

