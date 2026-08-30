from pygame import *
from Sprites import GameSprite

window = display.set_mode((700,500))
display.set_caption('Ping Pong Game')

background = transform.scale(image.load('background.jpg'), (700, 500))

clock = time.Clock()

left_pad = GameSprite('racket.png',
                      5, 200, 
                      50,100,
                      2)

runtime = True

while runtime :
    window.blit(background, (0,0))
    left_pad.reset(window)

    for e in event.get():
        if e.type == QUIT:
            runtime = False

    display.update()
    clock.tick(60)
