import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong Collision")
x1=540
y1=300
x2=20
y2=300
inward=True
while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(x1,y1,50,100))
    pygame.draw.circle(screen,(255,255,255),(x2,y2),10)
    if inward==True:
        x1-=3
        x2+=7
    if inward==False:
        x1+=3
        x2-=7
    if x2-10>=x1 and y1<=y2<=y1+100:
        inward=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()
