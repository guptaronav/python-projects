##print("Enter a String.")
##Str=input()
##if Str==Str[::-1]:
##    print("Given string is a palindrome.")
##else:
##    print("Given string is not a palindrome.")


##g="Welcome to Youngwonks!"
##print(g[0],g[1],g[2])
##print(g[-1])
##print(g[0:3])
##print(g[4:7])
##print(g[:4])
##print(g[4:])
##print(g[:])
##print(g[0:15:2])
##print(g[::3])
##print(g[::-1])


##Date="2/24/2021"
##Month, Day, Year=Date.split("/")
##print(Month, Day, Year)


##String="   Space   "
##Spaces = String.strip()
##print(len(String))
##print(len(Spaces))


##Wrd1="Hi"
##Wrd2="Bye"
##print(Wrd1+Wrd2)
##print(Wrd1*3)

##Str="Iteration"
##for i in Str:
##    print(i,end="-")


##print("Enter First Name")
##FN=input()
##print("Enter Last Name")
##LN=input()
##Username=FN[0]+". "+LN
##print(Username.lower())


##import pygame, sys, random, time
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500, 500))
##pygame.display.set_caption("Reaction Time Game")
##black, white = (0,0,0), (255,255,255)
##red=(255,0,0)
##colors = ['red','blue','gold','brown']
##
##def show(text):
##    font = pygame.font.SysFont('freesans',80)
##    msg = font.render(text, True, red)
##    screen.blit(msg,(250,200))
##random_text = random.choice(colors)
##
##while True:
##    random_color = random.choice(colors)
##    show(random_text)
##    pygame.draw.circle(screen,random_color, (320,500), 50)
##    clock.tick(60)
##
##    pygame.display.update()
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            sys.exit()
##        if event.type==KEYDOWN:
##            if random_text == random_color:
##                screen.fill()
##                print("GG You Won!")
##                random_text = random.choice(colors)





##monthstr="janfebmaraprmayjunjulaugsepoctnovdec"
##
##print("Enter a Month Number from 1 - 12")
##monthint=int(input())
##num=monthint*3
##print(monthstr[num-3:num])




##print("Enter a String.")
##Str=input()
##for i in Str:
##    print(ord(i))



##for i in range(33,257,1):
##    print(i,chr(i))



##import random
##secret=random.randint(1,100)
##print("Enter a Password.")
##pwd=input()
##Enc=[]
##Dec=[]
##for letter in pwd:
##    Enc.append(ord(letter)*secret)
##print(Enc)
##for item in Enc:
##    Dec.append(chr(item))
##print(Dec)



##dateStr = '12/12/2015'
##date = dateStr.split("/")
##greeting = "Hello How Are You ?"
##name = "Ronav Gupta"
##full_name = name.split()
##
##print(greeting.split(), full_name, "Today is", date)

##print("Enter a String of Numbers with Spaces In Between")
##NumStr=input()
##List=NumStr.split()
##for i in List:
##    if int(i)%2==0:
##        print(i)

##print("ENTER A STRING OF WORDS WITH COMMAS IN BETWEEN PLEASE")
##CommaStr=input()
##List=CommaStr.split(",")
##for word in List:
##    print(word)




#1

##print("Enter a String")
##String=input()
##print(String.title())

#2
##print(String.lower())



#3
##print("Enter String No. 1")
##String1=input()
##print("Enter String No. 2")
##String2=input()
##
##def Uppercase(S1,S2):
##    print(S1.upper())
##    print(S2.upper())
##
##Uppercase(String1,String2)


#4
##print("Enter String No. 1")
##String1=input()
##print("Enter String No. 2")
##String2=input()
##
##def reverse(S):
##    Chars=list(S)
##    for c in Chars:
##        if c.isupper():
##            print(c.lower(),end="")
##        else:
##            print(c.upper(),end="")
##    print()
##def print_reverse(S1,S2):
##    reverse(S1)
##    reverse(S2)
##
##print_reverse(String1,String2)


#5
##print("Enter String No. 1")
##String1=input()
##print("Enter String No. 2")
##String2=input()
##
##def reverse(S):
##    S=S.replace(' ','#')
##    Chars=list(S)
##    for c in Chars:
##        if c.isupper():
##            print(c.lower(),end="")
##        else:
##            print(c.upper(),end="")
##    print()
##def print_reverse(S1,S2):
##    reverse(S1)
##    reverse(S2)
##
##print_reverse(String1,String2)





##lenlist=[]
##charlist=[]
##print("Enter your 1st Word.")
##char1=input()
##len1=len(char1)
##charlist.append(char1)
##print("Enter your 2nd Word.")
##char2=input()
##len2=len(char2)
##charlist.append(char2)
##print("Enter your 3rd Word.")
##char3=input()
##len3=len(char3)
##charlist.append(char3)
##lenlist.append(len1)
##lenlist.append(len2)
##lenlist.append(len3)
##var=max(lenlist)
##length=len1+len2+len3
###print(var)
###print(charlist)
##for c in charlist:
##    if len(c)==var:
##        ans=c+"\n"
##        print(ans*length)




counter=-1
print("Enter a Name")
name=input()
#name="Ronav Gupta"
print(name[0])
print(name[::-1])
print(name.upper())
print(name.title())
print(name[-3:])
print(name.replace("a","l"))
for c in name:
    print(c)
if name==name[::-1]:
    print("PALINDROME!")
else:
    print("Palindrome False")
print(name.endswith("ing"))
for c in name:
    counter+=1
    print(c,end="")
    print(counter)










































































































