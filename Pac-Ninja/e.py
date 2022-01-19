import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Pac-Ninja")
frames1=[]
frames2=[]
Start=False
count1=0
count2=0
move=120
jump=250
jump2=250
move2=1080
fill=True
fill2=True
def Ninja():
    global count1,move,jump,fill
    if fill:
        screen.fill((5, 250, 120))
    if count1<27:
        for i in range(count1-2,count1+1):
            if i>=0:
                x=frames1[i].copy()
                screen.blit(x,(move-(count1-i)*15,jump))
    pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
    clock.tick(10)
    if 19<=count1<23:
        jump-=6
    if 23<=count1<27:
        jump+=6
    if move>=15*27+120:
        move=15*27+120
        fill=False
    else:
        move+=15
    if count1 == len(frames1):
        i=pygame.image.load("Idle__000.png")
        resize=pygame.transform.scale(i,(70,100))
        screen.blit(resize,(move,250))
        pygame.display.update()
        return
    else:
        count1+=1
    pygame.display.update()
    Ninja()

def Zombie():
    global count2,move2,jump2,fill2
    if fill2:
        screen.fill((5, 250, 120))
    if count2<27:
        for i in range(count2,count2+1):
            if i>=0:
                y=frames2[i].copy()
                screen.blit(y,(move2-(count2-i)*15,jump2))
    if 20<=count2<27:
        jump2=260
    pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
    clock.tick(10)
    if move2<=15*27+270:
        move2=15*27+270
        fill2=False
    else:
        move2-=15
    if count2 == len(frames2):
        fill2=False
        i=pygame.image.load("Dead (12).png")
        resize=pygame.transform.scale(i,(100,100))
        screen.blit(resize,(move2,260))
        pygame.display.update()
        return
    else:
        count2+=1
    pygame.display.update()
    Zombie()
#Ninja    
for n in range(1,10,1):
    i=pygame.image.load("Run__00"+ str(n)+".png")
    resize=pygame.transform.scale(i,(100,100))
    frames1.append(resize)
    
for n in range(1,10,1):
    i=pygame.image.load("Slide__00"+ str(n)+".png")
    resize=pygame.transform.scale(i,(100,100))
    frames1.append(resize)
    
for n in range(1,10,1):
    i=pygame.image.load("Jump_Throw__00"+ str(n)+".png")
    resize=pygame.transform.scale(i,(100,100))
    frames1.append(resize)


#Zombie
for n in range(1,10,1):
    i=pygame.image.load("Walk ("+ str(n)+").png")
    resize=pygame.transform.scale(i,(100,100))
    frames2.append(resize)

for n in range(1,9,1):
    i=pygame.image.load("Attack ("+ str(n)+").png")
    resize=pygame.transform.scale(i,(100,100))
    frames2.append(resize)

for n in range(1,13,1):
    i=pygame.image.load("Dead ("+ str(n)+").png")
    resize=pygame.transform.scale(i,(100,100))
    frames2.append(resize)
    
clock=pygame.time.Clock()
#print(len(frames1))
while True:
    screen.fill((5, 250, 120))
    if Start:
        Ninja()
        Zombie()

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                screen.fill((5, 250, 120))
                Start=True
    pygame.display.update()
