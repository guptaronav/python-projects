##print("Enter your age")
##Age = int(input())
##if Age > 16:
##    print("You are eligible to drive")
##else:
##    print("Sorry, you can't drive yet. You must wait", 16 - Age, "years")

##print("Enter your name")
##Name = input()
##print("Enter your gender")
##Gender = input()
##if Gender == "Male":
##    print("Hello Mr.", Name)
##elif Gender == "Female":
##    print("Hello Mrs.", Name)


##print("Enter a number")
##Num = int(input())
##if Num % 2 == 0:
##    print("Even")
##else:
##    print("Odd")

##print("Enter a score")
##Score = int(input())
##if Score >= 90 and Score <= 100:
##    print("Grade = A")
##if Score >= 80 and Score <= 89:
##    print("Grade = B")
##if Score >= 70 and Score <= 79:
##    print("Grade = C")
##if Score >= 60 and Score <= 69:
##    print("Grade = D")
##if Score >= 0 and Score <= 59:
##    print("Grade = F")

##print("Enter a speed at which a footbal is kicked towards a goalpost")
##Speed = int(input())
##if 0<Speed<=40:
##    print("Saved!")
##elif Speed>40 and Speed<=50:
##    print("Good Try!")
##elif Speed>50 and Speed<200:
##    print ("Goal!")
##else:
##    print("Fail")

##a = 3
##if a<1:
##    print("hello")
##elif a==2:
##    print("world")
##elif a==0:
##    print("john")
##else:
##    print("alice")
    
##print("Enter your age")
##Age = int(input())
##print("Enter your grade")
##Grade = int(input())
##if Age>=8 and Grade>=3:
##    print("You're eligible to play the game.")
##else:
##    print("You're not eligible to play the game.")

##print("Please enter a number")
##num = int(input())
##if num < 5:
##    print("hello")
##elif num > 10:
##    print("world")
##elif 1<num<8:
####    print("ronav")
##
##print("What state do you live in?")
##State = input()
##if State=="California" or State=="Oregon" or State=="Washington":
##
##    print("We suggest you to go for a coastal drive")
##else:
##    print("You may be better off skiing")
##


##print("Do you have an upcoming vacation?")
##Ans = input()
##if Ans=="Yes":
##    print("What grade are you in?")
##    Grade = int(input())
##    if Grade!=12:
##        print("Have an adventurous vacation")
##    elif Grade==12:
##        print("Great time to study for SAT")
##else:
##    print("Study hard at school")
##


##print("Enter a year")
##Year = int(input())
##if Year%4==0:
##    print("It is a leap year")


##print("Enter your Salary")
##Salary = int(input())
##print("Enter your year of service")
##YOS = int(input())
##Bonus = 5/100
##if YOS>5:
##    print(Bonus*Salary+Salary)
##else:
##    print("No Bonus!")
##

##print("Enter your gender")
##Gen = input()
##print("Enter your age")
##Age = int(input())
##if Gen=="F":
##    print("You only work in urban areas")
##elif Gen=="M" and 20<Age<40:
##    print("You can work anywhere")
##elif Gen=="M" and 40<Age<60:
##    print("You only work in urban areas")
##else:
##    print("ERROR")


print("Would you like to purchase Dairy or Fruits?")
Item = input()
if Item=="Dairy":
    print("We have milk, yogurt, butter, cheese")
    print("Which of these products would you like?")
    Dairy = input()
    if Dairy in "butter" or Dairy in "milk":
        print("It is 5$")
    elif Dairy in "yogurt" or Dairy in "cheese":
        print("It is 7$")
    else:
        print(Dairy,"is Out of Stock")
elif Item=="Fruits":
    print("I have apples, mangoes, strawberries and grapes")
    print("Choose from the options")
    Fruit = input()
    if "strawberries" in Fruit or "apples" in Fruit:
        print("It is 10$")
    elif "mangoes" in Fruit or "grapes" in Fruit:
        print("It is 12$")
    else:
        print(Fruit,"is Out of Stock")
    
