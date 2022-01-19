##print("Enter a Number")
##num1=int(input())
##print("Enter a Number")
##num2=int(input())
##print(num1+num2)

##print("Enter your Age")
##age=int(input())
##if 16<=age:
##    print("Did you pass the DMV test?")
##    dmv=input()
##    if dmv=="yes" or dmv=="Yes":
##        print("You can drive!")
##    else:
##        print("You need to take another test.")
##else:
##    print(16-age)
##

##print("Enter a Number")
##num=int(input())
##if num%5==0 and num%2==0 and num>5:
##    print(num/5+num/2)
##elif num%2==0 and num%5!=0:
##    print(num/2)
##elif num%5==0 and num%2!=0:
##    print(num/5)

##print("Enter a passcode")
##Password = input()
##if 10<len(Password)<15:
##    print("Intermediate Password")
##elif 1<len(Password)<10:
##    print("Weak Password")
##elif len(Password)>15:
##    print("Strong Password")
##elif len(Password)<=1:
##    print("INVALID")

##print("Would you like meat, pasta, or seafood?")
##Food = input()
##if Food=="meat":
##    print("Choose steak, pork chop, or roasted chicken")
##elif Food=="pasta":
##    print("Choose carbonara, spaghetti, or pesto")
##elif Food=="seafood":
##    print("Choose baked lobster, shrimp boil, or chili crab")


##import random
##tries=0
##num=random.randint(1,10)
##while True:
##    print("Enter a Guess")
##    guess=int(input())
##    if guess==num:
##        break
##    else:tries+=1
##print("You answered correctly after",tries,"attempts!")
    

##counter=0
##print("Enter a Number")
##num=int(input())
##while True:
##    counter+=1
##    if counter*counter==num:
##        break
##    else:
##        print("Perfect Square Not Identified Yet...")
##print("True!")


##number=0
##print("How many numbers?")
##numcount=int(input())
##for i in (numcount):
##    print("Enter a Number")
##    num=int(input()
##    number=num+number
##print(num)

answers=[]
import random
while len(answers)<=10:
    a=random.randint(1,100)
    if a%3==0:
        if a%2!=0:
            answers.append(a)
print(answers)




















