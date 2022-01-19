import pygame
from pygame.locals import *
import random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Flappy Bird")
y=300
x=300
e=random.randint(1,2)
obstaclewidth=30
rect1x=560
rect2x=560
rect1y=0
rect2y=600
counter=0
start=False
flymode=False
obstacleheight=random.randint(100,265)
score=0
counter=0
counter2=0
n=None
def show_text(msg,scorex,scorey,color):
        fontobj=pygame.font.SysFont("test", 32, bold=True)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(scorex,scorey))
while True:
    screen.fill((0,0,0))
    show_text(str(round(score)),290,55,(225,15,0))
    tp=pygame.draw.rect(screen,(0, 215, 25),(rect1x,rect1y, obstaclewidth, obstacleheight))
    bp=pygame.draw.rect(screen,(0, 215, 25),(rect2x,rect2y, obstaclewidth, obstacleheight-500))
    space=pygame.draw.rect(screen,(0,0,0),(rect1x,obstacleheight,1,100))
    bird=pygame.draw.circle(screen,(255,255,0),(x,y),20)
    counter+=1
    rect1x-=1
    rect2x=rect1x
##    if score%300==0:
##            score=score/300
    if bird.colliderect(space) and x==rect1x:
        score+=1
    if rect1x<=0:
        rect1x=560
        obstacleheight=random.randint(100,265)
    if counter>1 and start==True and flymode==False:
        y+=1
    if y>=600:
        x=300
        y=300
    if x>=600:
        x=300
        y=300
    if tp.colliderect(bird) or bp.colliderect(bird):
        print("You Died.")
        break
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                flymode=True
                start=True
                counter+=1
                y=y-10
                x+=7
        if event.type==KEYUP:
            if event.key==K_SPACE:
                flymode=False
    pygame.display.update()
