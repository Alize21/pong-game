import pygame

class Button:

    def __init__(self,x,y,image,scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image,(int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.action = False

    def click(self):

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.action = True

        if self.action:
            self.action = False
            return True
        
    def draw_image(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
