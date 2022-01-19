import pygame
from pygame.locals import *
import random
import time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((255,255,255))
counter=0
mousex=mousey=0
one=True
two=True
three=True
four=True
five=True
six=True
seven=True
eight=True
nine=True
a=None
b=None
c=None
d=None
e=None
f=None
g=None
h=None
i=None
end=False
def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont("test", 32, bold=True)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
def xee(x1,y1,x2,y2,x3,y3,x4,y4):
    pygame.draw.line(screen,(0,0,0),(x1,y1),(x2,y2),3)
    pygame.draw.line(screen,(0,0,0),(x3,y3),(x4,y4),3)
def o(x,y):
    pygame.draw.circle(screen,(0,0,0),(x,y),76,3)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN:
            counter+=1
            if event.button==1:
                mousex,mousey=event.pos
                print(mousex,mousey)
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),3)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),3)
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),3)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),3)
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),3)
    if 0<mousex<200 and 0<mousey<200 and one:
        one=False
        if counter!=0:
            if counter%2==0:
                a="o"
                o(100,100)
            else:
                a="x"
                xee(20,20,180,180,180,20,20,180)
    if 200<mousex<400 and 0<mousey<200 and two:
        two=False
        if counter!=0:
            if counter%2==0:
                b="o"
                o(300,100)
            else:
                b="x"
                xee(220,20,380,180,380,20,220,180)
    if 400<mousex<600 and 0<mousey<200 and three:
        three=False
        if counter!=0:
            if counter%2==0:
                c="o"
                o(500,100)
            else:
                c="x"
                xee(420,20,580,180,580,20,420,180)
    if 0<mousex<200 and 200<mousey<400 and four:
        four=False
        if counter!=0:
            if counter%2==0:
                d="o"
                o(100,300)
            else:
                d="x"
                xee(20,220,180,380,180,220,20,380)
    if 200<mousex<400 and 200<mousey<400 and five:
        five=False
        if counter!=0:
            if counter%2==0:
                e="o"
                o(300,300)
            else:
                e="x"
                xee(220,220,380,380,380,220,220,380)
    if 400<mousex<600 and 200<mousey<400 and six:
        six=False
        if counter!=0:
            if counter%2==0:
                f="o"
                o(500,300)
            else:
                f="x"
                xee(420,220,580,380,580,220,420,380)
    if 0<mousex<200 and 400<mousey<600 and seven:
        seven=False
        if counter!=0:
            if counter%2==0:
                g="o"
                o(100,500)
            else:
                g="x"
                xee(20,420,180,580,180,420,20,580)
    if 200<mousex<400 and 400<mousey<600 and eight:
        eight=False
        if counter!=0:
            if counter%2==0:
                h="o"
                o(300,500)
            else:
                h="x"
                xee(220,420,380,580,380,420,220,580)
    if 400<mousex<600 and 400<mousey<600 and nine:
        nine=False
        if counter!=0:
            if counter%2==0:
                i="o"
                o(500,500)
            else:
                i="x"
                xee(420,420,580,580,580,420,420,580)
    if a==b==c=="x":
        print("Player X Wins!")
        show_text("Player X Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(5,100),(595,100),3)
        end=True
    if a==b==c=="o":
        show_text("Player O Wins",215,300,(225, 15, 0))
        print("Player O Wins!")
        pygame.draw.line(screen,(0,0,0),(5,100),(595,100),3)
        end=True
    if d==e==f=="x":
        show_text("Player X Wins",215,300,(225, 15, 0))
        print("Player X Wins!")
        pygame.draw.line(screen,(0,0,0),(5,300),(595,300),3)
        end=True
    if d==e==f=="o":
        show_text("Player O Wins",215,300,(225, 15, 0))
        print("Player O Wins!")
        pygame.draw.line(screen,(0,0,0),(5,300),(595,300),3)
        end=True
    if g==h==i=="x":
        print("Player X Wins!")
        show_text("Player X Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(5,500),(595,500),3)
        end=True
    if g==h==i=="o":
        show_text("Player O Wins",215,300,(225, 15, 0))
        print("Player O Wins!")
        pygame.draw.line(screen,(0,0,0),(5,500),(595,500),3)
        end=True
    if a==d==g=="x":
        print("Player X Wins!")
        show_text("Player X Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(100,5),(100,595),3)
        end=True
    if a==d==g=="o":
        print("Player O Wins!")
        show_text("Player O Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(100,5),(100,595),3)
        end=True
    if b==e==h=="x":
        show_text("Player X Wins",215,300,(225, 15, 0))
        print("Player X Wins!")
        pygame.draw.line(screen,(0,0,0),(300,5),(300,595),3)
        end=True
    if b==e==h=="o":
        show_text("Player O Wins",215,300,(225, 15, 0))
        print("Player O Wins!")
        pygame.draw.line(screen,(0,0,0),(300,5),(300,595),3)
        end=True
    if c==f==i=="x":
        print("Player X Wins!")
        show_text("Player X Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(500,5),(500,595),3)
        end=True
    if c==f==i=="o":
        show_text("Player O Wins",300,(225, 15, 0))
        print("Player O Wins!")
        pygame.draw.line(screen,(0,0,0),(500,5),(500,595),3)
        end=True
    if a==e==i=="x":
        print("Player X Wins!")
        show_text("Player X Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(5,5),(595,595),3)
        end=True
    if a==e==i=="o":
        print("Player O Wins!")
        show_text("Player O Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(5,5),(595,595),3)
        end=True
    if c==e==g=="x":
        show_text("Player X Wins",215,300,(225, 15, 0))
        print("Player X Wins!")
        pygame.draw.line(screen,(0,0,0),(5,595),(595,5),3)
        end=True
    if c==e==g=="o":
        print("Player O Wins!")
        show_text("Player O Wins",215,300,(225, 15, 0))
        pygame.draw.line(screen,(0,0,0),(5,595),(595,5),3)
        end=True
    if one==False and two==False and three==False and four==False and five==False and six==False and seven==False and eight==False and nine==False:
        print("Draw!")
        show_text("DRAW!!!",215,300,(225, 15, 0))
        end=True
        
    pygame.display.update()
    if end:
        pygame.quit()
        exit()
    
