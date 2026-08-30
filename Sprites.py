from pygame import *

class GameSprite(sprite.Sprite):
    ''' Constructor ''' 
    def __init__(self, player_image, player_x, 
                 player_y, size_x, 
                 size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self, win_obj):
        win_obj.blit(self.image, (self.rect.x, self.rect.y))
    
    def left_paddle(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 305:
            self.rect.y += self.speed

    def right_paddle(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] amd self.rect.y > 305:
            self.rect.y += self.speed
