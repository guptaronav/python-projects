import pygame
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Pac–Ninja")
frames1=[]
frames2=[]
Idle=False
Run=False
Slide=False
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
jump=250
move=120
move2=1080



while True:
    clock=pygame.time.Clock()
    if Idle:
        move=120
        for n in range(1,10,1):
            i=pygame.image.load("Run__00"+ str(n)+".png")
            if count1 >= len(frames1):
                count1=0
            resize=pygame.transform.scale(i,(100,100))
            frames1.append(resize)
            screen.fill((5, 250, 120))
            pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
            screen.blit(frames1[count1],(move,250))
            move+=20
            count1+=1
            clock.tick(10)
            pygame.display.update()
        Idle=False
        for n in range(1,10,1):
            i=pygame.image.load("Slide__00"+ str(n)+".png")
            if count2 >= len(frames2):
                count2=0
            resize=pygame.transform.scale(i,(100,100))
            frames2.append(resize)
            screen.fill((5, 250, 120))
            pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
            screen.blit(frames2[count2],(move,250))
            jump+=5
            move+=16
            count2+=1
            clock.tick(10)
            pygame.display.update()
        for n in range(1,10,1):
            i=pygame.image.load("Throw__00"+ str(n)+".png")
            if count3 >= len(frames3):
                count3=0
            resize=pygame.transform.scale(i,(100,100))
            frames3.append(resize)
            screen.fill((5, 250, 120))
            pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
            screen.blit(frames3[count3],(move,250))
            #jump+=25
            count3+=1
            clock.tick(10)
            pygame.display.update()


        move2=1080
        for n in range(1,11,1):
                i=pygame.image.load("Walk ("+ str(n)+").png")
                if count5 >= len(frames5):
                    count5=0
                resize=pygame.transform.scale(i,(100,100))
                frames5.append(resize)
                screen.fill((5, 250, 120))
                pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
                screen.blit(frames5[count5],(move2,250))
                #jump+=5
                move2-=38
                count5+=1
                clock.tick(7)
                pygame.display.update()
        for n in range(1,9,1):
                i=pygame.image.load("Attack ("+ str(n)+").png")
                if count6 >= len(frames6):
                    count6=0
                resize=pygame.transform.scale(i,(100,100))
                frames6.append(resize)
                screen.fill((5, 250, 120))
                pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
                screen.blit(frames6[count6],(move2,250))
                #jump+=25
                count6+=1
                clock.tick(10)
                pygame.display.update()
        for n in range(1,13,1):
                i=pygame.image.load("Dead ("+ str(n)+").png")
                if count7 >= len(frames7):
                    count7=0
                resize=pygame.transform.scale(i,(100,100))
                frames7.append(resize)
                screen.fill((5, 250, 120))
                pygame.draw.line(screen,(0,0,0),(0,350),(1200,350),4)
                screen.blit(frames7[count7],(move2,260))
                #jump+=25
                count7+=1
                clock.tick(10)
                pygame.display.update()
        Idle=False
        

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_w:
                screen.fill((5, 250, 120))
                Run=True
##            if event.key==K_h:
##                Run=True
##            if event.key==K_y:
##                Slide=True
    pygame.display.update()

