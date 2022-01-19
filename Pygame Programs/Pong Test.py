import pygame
from pygame.locals import *
import dottedline
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")
up=False
down=False
w=False
s=False
x=300
y=300
x1=540
y1=300
x2=20
y2=300
clock=pygame.time.Clock()
flip=False
flip2=False
P1=0
P2=0
x3=250
y3=50
color=(0,0,0)
counter=0
#x,y=ball & x1,y1=paddle1 & x2,y2=paddle2
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("test",64)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
while True:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),(x1,y1,20,150))
    pygame.draw.rect(screen,(0,0,0),(x2,y2,20,150))
    pygame.draw.circle(screen,(0,0,0),(x,y),10)
    show_text(str(P1),x3,y3,color)
    show_text(str(P2),x3+100,y3,color)
    if up==True:
        y1-=5
    elif down==True:
        y1+=5
    if w==True:
        y2-=5
    elif s==True:
        y2+=5
    if y1<=10:
        up=False
        y1=10
    if y1>=440:
        down=False
        y1=440
    if y2<=10:
        w=False
        y2=10
    if y2>=440:
        s=False
        y2=440
    if x>=580:
        P1+=1
        x=300
        y=300
    if x<=20:
        P2+=1
        x=300
        y=300
    if x-10>=x1 and y1<=y<=y1+150:
        flip=True
    if x-10<=x2 and y2<=y<=y2+150:
        flip=False
    if y==600 and 0<=x<=600:
        flip2=True
    if y==5 and 0<=x<=600:
        flip2=False
    if flip:
        x-=5
    else:
        x+=5
    if flip2:
        y-=5
    else:
        y+=5
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                up=True
            if event.key==K_DOWN:
                down=True
            if event.key==K_w:
                w=True
            if event.key==K_s:
                s=True
        if event.type==KEYUP:
            if event.key==K_UP:
                up=False
            if event.key==K_DOWN:
                down=False
            if event.key==K_w:
                w=False
            if event.key==K_s:
                s=False
    for lines in range(0,1200,50):
        pygame.draw.rect(screen,(0,0,0),(300,lines,10,25))
    pygame.display.update()
    clock.tick(25)

