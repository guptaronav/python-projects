##fruit=['apple','grape','banana','orange','mango']
##print(fruit[3])
##fruit.pop(3)
##fruit.remove('banana')
##print(fruit)

##numbers=[1,2,3,4,5]
##numbers.append(100)
##numbers.pop(2)
##numbers.reverse()
##print(numbers)

##import random
##Random=[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
##for i in range(1,11,1):
##    Random.append(random.randint(1,100))
##Random.sort(reverse=1)
##print(Random)

##fruit=['apple','grape','banana','orange','mango']
##A=fruit.pop(2)
##print(A)
##print(fruit)

##Friends=['A','B','C','D','E']                                         #listname=[item1,item2…] - is used to create lists.
##print(len(Friends))

##print(Friends[1])                                                     #listname[indexposition] - is used to print a specific item of the list.

##print(Friends[1:3])                                                   #listname[startindexposition:stopindexposition] - is used to print a specific range of items in the list.

##Friends[2]='F'                                                        #listname[indexposition]=new_value - is used to update or replace an item in the list.
##print(Friends)


##Friends.insert(3,'G')                                                 #listname.insert(indexposition,new_value) - is used to insert an item in the list at a specific position.
##print(Friends)

##Friends.append('H')                                                   #listname.append(new_value) - is used to add an item to the end of the list.
##print(Friends)


##Friends.pop(3)                                                        #listname.pop(indexposition) - is used to remove an item in the list with a certain position.
##print(Friends)

##Friends.remove('E')                                                   #listname.remove(value) - is used to remove an item in the list with a certain value.
##print(Friends)


##t=Friends.pop(4)                                                      #variablename=listname.pop(indexposition) - is used to extract a specific item from the list and store it into a variable.
##print(t)


##Friends.sort()                                                        #listname.sort() - is used to sort the list into alphabetical order if letters and into numerical order if numbers.
##print(Friends)


##Friends.reverse()                                                     #listname.reverse() - is used to flip the entire list backwards.
##print(Sdneirf)


##empty=[]                                                              #new_listname=old_listname.copy() - is used to transfer items from one list to another.
##fruit=['apple','grape','banana','orange','mango']
##empty=fruit.copy()
##print(empty)


##Hello=[]                                                              #listname=variablename.split() - is used to split a string into a list that consists of seperate words.
##Greetings="Hello, how are you?"
##Hello=Greetings.split()
##print(Hello)


##Hello=[]
##Greetings="Hello, how are you?"                                       #listname=list(variablename) - is used to split a variable into a list that consists of seperate letters, punctuation, and spaces.
##Hello=list(Greetings)
##print(Hello)


##Greetingletters=['H', 'e', 'l', 'l', 'o', ',',' ','h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']        #variablename="".join(listname) - is used to join a list into a variable.
##Hellostring="".join(Greetingletters)
##print(Hellostring)


##import random                                                         #min(listname) or max(listname) - is used for printing the maximum and minimum of a list.
##Numbers=[]
##for i in range(1,21,1):
##    num=random.randint(1,100)
##    Numbers.append(num)
##print(Numbers)
##print(min(Numbers))                
##print(max(Numbers))



##import random
##Dice=['1','2','3','4','5','6',]
##for i in range(1,7,1):
##    random.shuffle(Dice)
##print(Dice[0])



##import random
##CC=['Tom','Jerry','Tom 2','Jerry 2','Tom 3','Jerry 3']
##A=random.choice(CC)
##print(A)



##import random
##CC=['Tom','Jerry','Tim','Jimmy','Tammy','Jim']
##Storage=[]
##Storage=random.sample(CC,3)
##print(Storage)




##import random
##fruits=['orange','apple','banana','pomegranite','pineapple','mango','grapes']
##for i in fruits:
##    while "p" in i:
##        print(i)
##        break


##import random
##
###Sports=['Basketball','Soccer','Cricket','Tennis','Football']
##Chances=7
##Underlines=[]
##def picklePicker():
##    word_file = "/usr/share/dict/words"
##    WORDS = open(word_file).read().splitlines()
##    return random.choice(WORDS)
##Answer=picklePicker()
##def printSport(s):
##    for i in s:
##        print(i," ",end="")
##    print()
##
###Answer=picklePicker().lower()
##Letters=list(Answer)
##
##for i in Letters:
##    Underlines.append("_")
##printSport(Underlines)
##
##        
##def find(s, ch):
##    Indexes=list()
##    i=0
##    for char in s:
##        if char==ch:
##            Indexes.append(i)
##        i+=1
##    return Indexes
##print(Answer)
##while True:
##    print("Guess a Letter!")
##    Guess=input()
##    Guess=Guess.lower()
##    if Guess in Answer:
##        Found_Indexes=find(Answer, Guess)
##        for i in Found_Indexes:
##            Underlines[i]=Guess
##    else:
##        Chances-=1
##        if Chances>1:
##            print("You have",Chances,"chances left.")
##        else:
##            print("You have",Chances,"chance left.")
##    printSport(Underlines)
##    if Chances<=0:
##        print("You Lost. The answer was",Answer)
##        break
##    if Underlines==Letters:
##        print("You Won")
##        break
    


##import random
##Chances=7
##Underlines=[]
##Sports=['Basketball','Soccer','Cricket','Tennis','Football']
##Answer=random.choice(Sports)
##Letters=list(Answer)
##for i in range(0,len(Letters),1):
##    Underlines.append("_")
##print(Underlines)
##while True:
##    print("Guess a Letter.")
##    Guess=input()
##    for n in range(0,len(Letters),1):
##        if Guess==Letters[n]:
##            Underlines[n]=Guess
##            print(Underlines)
##            print("Correct, Go Ahead")
##    if Guess not in Letters:
##        Chances-=1
##        print("Wrong, Try Again")
##    if "_" not in Underlines:
##        print("You Won!")
##        break
##    if Chances<=0:
##        print("You Lost!")
##        break
    


##Numbers=[1,2,3,4,5,6]
##for i in range(0,len(Numbers),1):
##    print(Numbers[i],end="")


##NUMPILE=(1,4,2,3,7,5,6,8,0,7,9,8,9,5,3,5,2,7)
##print(NUMPILE[1:5])

##SportTuple=("Basketball","Baseball","Football","Soccer","Cricket")
##Sport=list(SportTuple)
##print(Sport)

##Grades=[]
##Subjects=['Math','ELA','Science','History']
##Tom=[92,88,100,76]
##Jerry=[88,77,86,99]
##Jack=[92,76,68,54]
##Grades.append(Tom)
##Grades.append(Jerry)
##Grades.append(Jack)
##print(Grades)
##print("Tom's",Subjects[3],"Grade is",str(Grades[0][3])+"/100")
##Subj=input("Enter A Subject: ")
##if Subj==Subjects[0]:
##    print("The average grade is…",(Grades[0][0]+Grades[1][0]+Grades[2][0])/3+"/100")
##if Subj==Subjects[1]:
##    print("The average grade is…",(Grades[0][1]+Grades[1][1]+Grades[2][1])/3+"/100")
##if Subj==Subjects[2]:
##    print("The average grade is…",(Grades[0][2]+Grades[1][2]+Grades[2][2])/3+"/100")
##if Subj==Subjects[3]:
##    print("The average grade is…",(Grades[0][3]+Grades[1][3]+Grades[2][3])/3+"/100")

##import random
##Store=[]
##for i in range(1,21,1):
##    Ranum=random.randint(1,100)
##    Store.append(Ranum)
##Store.sort(reverse=1)
##print(Store[1])

##Sports=['Basketball','Soccer','Cricket','Tennis','Football']
##print("Enter A Letter")
##Letter=input()
##for i in Sports:
##    if Letter in i:
##        print(i,i.index(Letter))

import turtle
import random

t = turtle
screen = turtle.getscreen()

def initialize(): #This sets up the background and settings for the game
    global word
    t.speed(0) #This creates the settings
    screen.tracer(0)
    t.hideturtle()
    t.setworldcoordinates(20,20,80,80)

    t.penup() #This draws a gallow
    t.setpos(55,45)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)

    t.penup()
    t.setpos(35,30)
    t.left(90)
    for i in range(len(word)): #This draws the underscores for letters
        t.pendown()
        t.forward(2)
        t.penup()
        t.forward(2)

def drawLetter(word,character): #Called when player correctly guesses. Draws letter
    global count
    times = [x for x, appearance in enumerate(word) if appearance == character] #Creates list of when 'character' appears in 'word'
    for i in range(len(times)): #Draws character based on when it appears in 'word'
        t.penup()
        t.setpos(36 + 4*(times[i]),31)
        t.write(character, move=True, align='center', font=('Arial', 20, 'normal'))
    count += len(times)

def drawBody(): #Called when player incorrectly guesses. Draws body part
    global n
    t.setheading(270)
    t.penup()
    if n == 0: #draws head
        t.setpos(45,60)
        t.right(90)
        t.pendown()
        t.circle(3,360,500)
        t.penup()
    elif n == 1: #draws torso
        t.setpos(45,54)
        t.pendown()
        t.forward(8)
        t.penup()
    elif n == 2: #draws left arm
        t.setpos(45,51)
        t.right(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 3: #draws right arm
        t.setpos(45,51)
        t.left(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 4: #draws left leg
        t.setpos(45,46)
        t.right(45)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 5: #draws right leg
        t.setpos(45,46)
        t.left(45)
        t.pendown()
        t.forward(6)
        t.penup()

def guess(): #This function asks the user for an input, and either draws a body part or a letter
    global word
    global n
    character = t.textinput('Your Guess','What letter are you thinkin\'')
    if character in word: #If letter is in word, draws letter
        drawLetter(word,character)
    else: #If letter not in word, draws body part
        drawBody()
        n += 1

def fake_main():
    global n
    global count
    global word
    n = 0
    count = 0
    initialize()
    done = False
    while not done:
        if n > 5:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('You lose.' + 'The word was \'' + word + '\'', move=True, align='center', font=('Arial', 50, 'normal'))
        elif count > len(word) - 1:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Amazing! You guessed the word \'' + word + '\'. You win!', move=True, align='center', font=('Arial', 30, 'normal'))
        else:
            guess()
    return None

def main():
    finished = False
    while not finished:
        global word
        wordList = ['kendrick','jcole','eminem','kanye','bigsean','travis','childish','drake','weeknd','twochainz','schoolboy','kidcudi','chance','migos','wakaflame','guccimane']
        word = wordList[random.randint(0,15)]
        fake_main()
        repeat = t.textinput('','Would you like to play again? (y/n): ')
        if repeat == 'y':
            t.reset()
        else:
            finished = True
    return None

main()
