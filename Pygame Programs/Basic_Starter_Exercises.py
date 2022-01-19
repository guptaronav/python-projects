##import pygame
##from pygame.locals import *
##pygame.init()
##screen=pygame.display.set_mode((600,600))
##pygame.display.set_caption("Rectangle")
##while True:
##    pygame.draw.rect(screen,(18, 243, 255),(200,200,200,100))
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen=pygame.display.set_mode((600,600))
##pygame.display.set_caption("Circle")
##while True:
##    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
##    pygame.draw.circle(screen,color,(300,300),29,5)
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen=pygame.display.set_mode((600,600))
##pygame.display.set_caption("Polygon")
##while True:
##    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
####    pygame.draw.line(screen,color,(100,100),(500,500))
####    pygame.draw.line(screen,color,(500,500),(100,500))
####    pygame.draw.line(screen,color,(100,500),(100,100))
##
##    pygame.draw.polygon(screen,color,((100,100),(100,500),(500,500)))
##
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import pygame
##from pygame.locals import *
##pygame.init()
##screen=pygame.display.set_mode((600,600))
##pygame.display.set_caption("Rectangle")
##while True:
##    pygame.draw.rect(screen,(18, 243, 255),(0,0,100,100),1)
##    pygame.draw.rect(screen,(18, 243, 255),(500,500,100,100),1)
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()



##import pygame
##from pygame.locals import *
##pygame.init()
##screen=pygame.display.set_mode((600,600),RESIZABLE)
##pygame.display.set_caption("Circle")
##while True:
##    screen.fill((217, 70, 2))
##    pygame.draw.circle(screen,(7, 242, 191),(0,0),45,3)
##    pygame.draw.circle(screen,(7, 242, 191),(600,600),45,3)
##    pygame.draw.circle(screen,(7, 242, 191),(0,600),45,3)
##    pygame.draw.circle(screen,(7, 242, 191),(600,0),45,3)
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()



##import pygame
##from pygame.locals import *
##pygame.init()
##screen=pygame.display.set_mode((900,900),RESIZABLE)
##pygame.display.set_caption("Da X")
##while True:
##    pygame.draw.line(screen,(7, 242, 191),(0,0),(900,900))
##    pygame.draw.line(screen,(7, 242, 191),(0,900),(900,0))
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()



#MUST MAKE A HOUSE AND A ROBOT FOR HW :)




































































