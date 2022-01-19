import pygame
from pygame.locals import *
import random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")
x=300
y=300
rflag=False
lflag=False
uflag=False
dflag=False
ax=round(random.randint(15,585)/15)*15
ay=round(random.randint(15,585)/15)*15
bx=round(random.randint(15,585)/15)*15
by=round(random.randint(15,585)/15)*15
head=[x,y]
snakelist=[]
snakelist.append(head)
score=0
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("test",64)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
while True:
    screen.fill((0,0,0))
    apple=pygame.draw.rect(screen,(225,0,0),(ax,ay,15,15))
    banana=pygame.draw.rect(screen,(225,255,0),(bx,by,15,15))
    i=0
    for i in snakelist:
        snake=pygame.draw.rect(screen,(0,215,25),i+[15,15])
    x=snakelist[0][0]
    y=snakelist[0][1]
    show_text(str(score),288,100,(0,255,255))
    if snake.colliderect(apple):
        snakelist.append([ax,ay])
        ax=random.randint(0,600)
        ay=random.randint(0,600)
        score+=1
    if snake.colliderect(banana):
        snakelist.append([bx,by])
        bx=random.randint(0,600)
        by=random.randint(0,600)
        score+=1
    if x>600:
        x=0
    if x<0:
        x=600
    if y<0:
        y=600
    if y>600:
        y=0
    if uflag==True:
        y-=3
    if dflag==True:
        y+=3
    if rflag==True:
        x+=3
    if lflag==True:
        x-=3
    snakelist.pop()
    snakelist.insert(0,[x,y])
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                uflag=True
                rflag=False
                lflag=False
                dflag=False
            if event.key==K_DOWN:
                dflag=True
                rflag=False
                lflag=False
                uflag=False
            if event.key==K_RIGHT:
                rflag=True
                lflag=False
                uflag=False
                dflag=False
            if event.key==K_LEFT:
                lflag=True
                uflag=False
                dflag=False
                rflag=False
    pygame.display.update()
    if [x,y] in snakelist[1:]:
        screen.fill((0,0,0))
        show_text("Game Over!",185,290,(255,0,255))
        pygame.display.update()
        break
    
