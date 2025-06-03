import pygame
pygame.init()
window=pygame.display.set_mode((400,300))
window.fill((255,255,255))
GR=(0,255,0)
pygame.draw.circle(window, GR, (100,100), 50, 3)
pygame.draw.circle(window, GR, (300,300), 50)
pygame.display.update()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    pygame.display.flip()

