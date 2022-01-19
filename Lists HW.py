##Animals=['Dog:','Cat:','Owl:','Duck:']
##Sounds=['Bark','Meow','Hoot Hoot!','Quack!']
##for i in range(0,4,1):
##    print((Animals[i]),(Sounds[i]))
         
##animals = ['lion', 'tiger', 'panda', 'bear', 'kangaroo', 'leopard']
##for i in range(1,6,2):
##    print(animals[i])


##animals = ['lion', 'tiger', 'panda', 'bear', 'kangaroo', 'leopard']
##for i in range(0,6,2):
##    print(animals[i])


##animals = ['lion', 'tiger', 'panda', 'bear', 'kangaroo', 'leopard','dog','cat']
##animals.sort(reverse=1)
##print(animals)


##import random
##A=[]
##for i in range(1,31,1):
##    B=random.randint(1,200)
##    A.append(B)
##print(A)
##
##for n in A:
##    if n%2==0:
##        print(n)


##Words=['lion', 'tiger', 'panda', 'bear', 'kangaroo', 'leopard','dog','cat']
##for i in Words:
##    if len(i)>5:
##        print(i)

##Words=['lion', 'tiger', 'panda', 'bear', 'kangaroo', 'leopard','dog','cat']
##for i in Words:
##    if "a" and "b" in i:
##        print(i)

##import random
##import time
##D=None
##Counter=0
##Card_Mode=["Defense","Offense"]
##print("Welcome to Battle Arena the Card Edition!")
##print("You're now, currently on the Battle Field! Make your move.")
##Lose="Nice Try, but You Lost!"
##Win="You Won!"
##Tie="You're still standing!"
##while True:
##    Counter+=1
##    print("Which Mode would you like to put the card you just drew into, Defense or Offense? (You can also Skip or Surrender) **Hint/Tip: IDK Mode will allow me to help you and choose a mode for you on that move. Although, don't waste your turns.**")
##    C=input()
##    A=random.randint(1,500)
##    B=random.randint(500,1000)
##    A1=random.randint(1,500)
##    B1=random.randint(500,1000)
##    E=[random.randint(1,1000)]
##    F=[random.randint(1,1000)]
##    Defense=[A or B]
##    Attack=[A1 or B1]
##    if C=="Defense":
##        print(Defense,"Defense Points")
##        D="Defense"
##    if C=="Offense":
##        print(Attack,"Attack Points")
##        D="Attack"
##    if C=="Skip":
##        print("You Passed Your Turn")
##        D=="Skip"
##        time.sleep(3) 
##    if C=="Surrender":
##        print("You Surrendered and Forfeit!")
##        break
##    if C=="IDK":
##        C=random.choice(Card_Mode)
##        print("Loading…")
##        time.sleep(2)
##        print("Connecting…")
##        time.sleep(1.5)
##    if C=="Defense":
##        print(Defense,"Defense Points")
##        D="Defense"
##    if C=="Offense":
##        print(Attack,"Attack Points")
##        D="Attack"
##    if D=="Attack" and Attack>E:
##        print(Win)
##        break
##    if D=="Attack" and Attack<E:
##        print(Lose)
##        break
##    if D=="Defense" and Defense<E:
##        print(Tie)
##    if D=="Defense" and Defense>E:
##        print(Win)
##        break
##    if D=="Defense" and Defense==E or Defense==F:
##        print(Tie)
##    if D=="Attack" and Attack==E or Attack==F:
##        print(Tie)
##    if D=="Attack" and Attack>F:
##        print(Lose)
##        break
##    if D=="Attack" and Attack<F:
##        print(Win)
##        break
##    if D=="Defense" and Defense>F:
##        print(Tie)
##    if D=="Defense" and Defense<F:
##        print(Tie)
##        
##for i in range(1,6,1):
##    print()
##print("You've exited the Battle Field and have left the Arena.")
##
