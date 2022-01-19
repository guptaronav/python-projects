##a=0
##while a!=50:
##    a+=1
##    print(a)

##a=20
##while a>=1:
##    print(a)
##    a=a-1
##while a<=35:
##    print(a)
##    a=a+1

##a=-17
##while a<=24:
##    print(a)
##    a+=1
##while a>=8:
##    print(a)
##    a-=1
##print("Bing!")

##while True:
##    print("Ronav")

##n = 0
##while True:
##    while n<=9:
##        n = n+1
##        print(n)
##    while n>=2:
##        n = n-1
##        print(n)

##import random
##import time
##while True:
##    A = random.uniform(1,100)
##    print(A)
##    time.sleep(3)

##A=5
##while A!=1:
##    A=A-1
##    print(A)
##print("Blast Off!")

##a=1
##while True:
##    print(a)
##    a+=1
##    if a==15:
##        print("Hello")
##        break

##import random
##import time
##Con=None
##Count=0
##print("How much money would you like to deposit in your account?")
##Money=int(input())
##while True:
##    Count+=1
##    if Count==1:
##        print("Would you like to roll the dice?")
##    else:
##        print("Would you like to roll the dice again?")
##    Die = input()
##    if Die=="Yes":
##        dice1=random.randint(1,6)
##        dice2=random.randint(1,6)
##    elif Die=="No" and Count==1:
##        print("You didn't roll the dice...")
##        break
##    elif Die=="No" and Count !=1:
##        print("You didn't roll the dice again...")
##        break
##    print("Waiting for a few seconds…")
##    time.sleep(2)
##    print("You rolled…",dice1,"and",dice2)
##    if dice1==dice2:
##        Money+=5
##        print("You Won","5 dollars","and have",Money,"dollars in total.")
##    else:
##        Money-=1
##        print("You Lost","and have",Money,"dollars in total.")
##    if Money==0:
##        print("Would you like to continue?")
##        Con=input()
##        if Con=="Yes":
##            print("Ok…")
##        if Con=="No":
##            print("Thank You For Playing")
##            break

##pwd1=None
##while True:
##    print("Enter the password")
##    pwd=input()
##    if pwd1==pwd:
##        print("Access Granted")
##        break
##    else:
##        print("Access Denied")

##import random
##while True:
##    A=random.randint(100,999)
##    print(A)
##    if A%23==0:
##        break


##import random
##Count=0
##A=random.randint(20,30)
##guess=None
##while A!=guess:
##    Count+=1
##    print("Enter a number")
##    guess=int(input())
##    if A==guess:
##        print(Count)

##while True:
##    print("Enter a word")
##    Word=input()
##    for i in range(0,len(Word),1):
##        print(Word[i])

##a=1
##while a<=50:
##    print(a)
##    a+=1

##import random
##a=0
##while a<=20:
##    b=random.random()
##    print(b)
##    a+=1

##A=10
##while A<=40:
##    print(A)
##    A+=1

##A=1
##while A<=50:
##    if A%7==0:
##        print(A)
##    A+=1

##A=50
##while A>=1:
##    print(A)
##    A-=1

##import random
##while True:
##    A=random.randint(1,50)
##    print(A)
##    if A%11==0:
##        break

##import random
##while True:
##    A=random.randint(20,100)
##    print(A)
##    if A==88:
##        break
    
####import random
####while True:
####    A=random.randint(20,100)
####    print(A)
####    if A%7==0 or A%9==0:
####        break

##A="Ronav"
##while True:
##    print("Enter a name")
##    B=input()
##    if A==B:
##        break

##for i in range(1,16,2):
##    print(i)

##print("Enter Your Name")
##A=input()
##for i in range(1,10,1):
##    print(A)
##    if i==4:
##        print("Hello!")

