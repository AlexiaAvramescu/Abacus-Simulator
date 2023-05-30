import pygame

pygame.init()

screen_color = (185,255,187)

screen=pygame.display.set_mode((1000,700))
screen.fill(screen_color)

class button(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(80,53))
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.visible = True

    def toggle_visibility(self):
        self.visible = not self.visible

    def draw(self):
        screen.blit(self.image, self.rect)
    def draw_screen2(self):
        screen.blit(self.image,self.rect)
class buttons_abac(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(250,150))
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.visible = True

    def draw(self):
        screen.blit(self.image, self.rect)


class button_meniu(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(55,30))
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.visible = True

    def draw(self):
        screen.blit(self.image, self.rect)

class button_exit(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(80,53))
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.visible = True

    def draw(self):
        screen.blit(self.image, self.rect)

class button_refresh(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(60,40))
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.visible = True

    def draw(self):
        screen.blit(self.image, self.rect)
