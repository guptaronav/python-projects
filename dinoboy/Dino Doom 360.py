import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Platformer Game (Dino Doom 360)")
walk=[]
count=0
x=300
y=300
right=False
left=False
jump=False
for n in range(1,11,1):
    i=pygame.image.load("Walk ("+ str(n)+").png")
    resize=pygame.transform.scale(i,(150,100))
    walk.append(resize)
while True:
    screen.fill((5, 225, 250))
    if right:
        x+=2
        count+=1
        screen.fill((5, 225, 250))
        f=walk[count]
        screen.blit(f,(x,y))
        if count==len(walk):
            count=0
        
    if count==len(walk):
        count=0
        
    screen.blit(resize,(x,y))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                right=True
            if event.key==K_LEFT:
                x-=2
                left=True
            if event.key==K_UP:
                y-=2
                jump=True
        if event.type==KEYUP:
            if event.key==K_RIGHT:
                right=False
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
