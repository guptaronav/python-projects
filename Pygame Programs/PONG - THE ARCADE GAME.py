import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")
paddle1={"x":50,"y":220,"rect":None}
paddle2={"x":550,"y":220,"rect":None}
ball={"x":300,"y":300,"rect":None}
speedx=speedy=2
up=down=w=s=False
def draw():
    global paddle1,paddle2,ball
    paddle1["rect"]=pygame.draw.rect(screen,(0,0,0),(paddle1["x"],paddle1["y"],20,150))
    paddle2["rect"]=pygame.draw.rect(screen,(0,0,0),(paddle2["x"],paddle2["y"],20,150))
    ball["rect"]=pygame.draw.circle(screen,(0,0,0),(ball["x"],ball["y"]),10)
def move():
    global paddle1,paddle2,up,down,w,s,speedy,speedx
    if paddle1["y"]<=10:
        up=False
    if paddle1["y"]>=440:
        down=False
    if paddle2["y"]<=10:
        w=False
    if paddle2["y"]>=440:
        s=False
    if ball["y"]==10:
        speedy*=-1
    if ball["y"]==440:
        speedy*=-1
    if ball["x"]==580 or ball["x"]==20:
        ball["x"]=300
        ball["y"]=300
    if up==True:
        paddle1["y"]-=5
    if down==True:
        paddle1["y"]+=5
    if w==True:
        paddle2["y"]-=5
    if s==True:
        paddle2["y"]+=5
    ball["x"]+=speedx
    ball["y"]+=speedy
while True:
    screen.fill((255,255,255))
    draw()
    move()
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
    pygame.display.update()
