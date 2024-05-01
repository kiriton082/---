from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
window.fill((0,0,255))

clock = time.Clock()
FPS = 30



class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, sizeX, sizeY):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (sizeX, sizeY))
       self.speed = player_speed
       self.speed_x = player_speed
       self.speed_y = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

score_1 = 0
class Enemy(GameSprite):
    def update(self):
        global score_1
        if self.rect.x <= 660 and self.rect.x >= 10:
            self.rect.x += self.speed_x
        if self.rect.y <= 460 and self.rect.y >= 10:
            self.rect.y += self.speed_y

        if self.rect.x == 660 or self.rect.x == 10:
            self.speed_x = self.speed_x*-1
            score_1 -= 1

        if self.rect.y == 460 or self.rect.y == 10: 
            self.speed_y = self.speed_y*-1
        

font.init()
font = font.SysFont("Arial", 30)

win = font.render('Ты всё таки победил..', True, (0, 255, 0))
lose = font.render('КАПЕЦ ):(', True, (255, 0, 0))

racket_1 = Player("rocket.png", 10, 390, 10, 30, 100)
racket_2 = Player("rocket.png", 660, 390, 10, 30, 100)
ball = Enemy("ball.png", 300, 250, 5, 30, 30)

finish = False
game = True
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0,0,255))

    racket_1.reset()
    racket_1.update_1()

    racket_2.reset()
    racket_2.update_2()

    ball.reset()
    ball.update()
    
    score = font.render('Счёт: ' + str(score_1), True, (255, 255, 255))
    window.blit(score, (300, 10))
    

    display.update()

    clock.tick(FPS)