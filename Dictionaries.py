
##ID = {"Age":9, "Gender":"Boy", "First Name":"Ronav"}
##ID["Last Name"]="Gupta"
##print(ID)
##key=input("Enter an ID Detail to get the answer: ")
##print(key+": "+str(ID[key]))

##Friends={"John":"Pasta","Max":"Soup","Jenny":"Noodles","Barry":"Berries"}
##print("Enter a Name of a Friend to get their Favorite Food.")
##Name=input()
##print("It's",Friends[Name])                                                               ##print(dictionaryname[key]) will print the value of the referred key.


##Friends={"John":"Pasta","Max":"Soup","Jenny":"Noodles","Barry":"Berries"}                 ##dictionaryname[newkey]="newvalue" will add a key and a value to the dictionary.
##Friends["Jane"]="Cupcakes"
##print(Friends)


##Friends={"John":"Pasta","Max":"Soup","Jenny":"Noodles","Barry":"Berries"}                 ##del(dictionaryname[key]) will delete a key and a value from the dictionary.
##del(Friends["John"])
##print(Friends)


##Friends={"John":"Pasta","Max":"Soup","Jenny":"Noodles","Barry":"Berries"}                 ##dictionaryname[existingkey]="newvalue" will update the specified existing key's value.
##Friends["Jenny"]="Burgers"
##print(Friends)


##Friends={"John":"Pasta","Max":"Soup","Jenny":"Noodles","Barry":"Berries"}                 ##for i in dictionaryname:
##for i in Friends:                                                                         ##print(i+":",dictionaryname[i]) will print each item in the dictionary one by one.
##    print(i+":",Friends[i])


##Fruities={"Mango":9,"Berries":5,"Pineapple":100,"Seeds":1,"Banana":99}                      ##for key,value in dictionaryname.items():
##for key,value in Fruities.items():                                                          ##if value==specificwantedvalue:
##   if value==100:                                                                           ##print(key) will print the specified corresponding key from its value.
##        print(key)


##import random
##Fruities={"Mango":9,"Berries":5,"Pineapple":100,"Seeds":1,"Banana":99}
##print("Enter a fruit's name")
##Chosen_Fruit=input()
##if Chosen_Fruit in Fruities:
##    print("$"+str(Fruities[Chosen_Fruit]))
##else:
##    Fruities[Chosen_Fruit]=random.randint(1,100)
##    print("$"+str(Fruities[Chosen_Fruit]))
    

##import random
##import time
##Foods={}
##print("Enter a food's name")
##Chosen_Food=input()
##Foods[Chosen_Food]=random.randint(1,100)
##print("Loading…")
##time.sleep(2)
##print("The Price is $"+str(Foods[Chosen_Food]))

##Passcode_Log = {"Jimmy":str(1234),"Jenny":"ABCD"+str(1234),"John":"ABCD","Jack":"1A2B3C4D","Jill":"!@#$%^&*()"}
##print("Enter a Username Please")
##Username=input()
##if Username in Passcode_Log:
##    print("Enter the Password")
##    Pwd=input()
##    if Pwd==Passcode_Log[Username]:
##        print("Access Granted")
##    else:
##        print("Access Denied")


##import random
##import time
##Counter=0
##Qs=[]
##Jackpot = {"What is air made of?":"78% Nitrogen and 21% Oxygen",
##           "What are sport items made of?":"Boron",
##           "What is poison made of?":"Arsenic",
##           "What is emerald made of?":"Beryllium",
##           "What is a battery made of?":"Zinc, Magnesium, and Potassium"}
##for i in Jackpot:
##    Qs.append(i)
##random.shuffle(Qs)
##for z in Qs:
##    print(z)
##    A=input()
##    if A==Jackpot[z]:
##        print("Correct!")
##        Counter+=1
##    else:
##        print("Wrong!")
##print("You got", Counter, "points!")



##Numbers={1:"",2:"",3:"",4:"",5:""}
##for i in Numbers:
##    Numbers[i]=i*i
##print(Numbers)


##Days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
##ASA=["HW","Maths","Reading and Coding", "Karate", "Gaming"]
##WeekWork={}
##for i in range(0,len(Days),1):
##    WeekWork[Days[i]]=ASA[i]
##print(WeekWork)


##Grades={"Joe":25,"Jason":40,"Jackson":50, "James":45,"Jace":30,"Jones":35}
##for i in Grades:
##    Grades[i]+=5
##print(Grades)


##Grades={"Joe":75,"Jason":90,"Jackson":60, "James":25,"Jace":100,"Jones":35}
##for i in Grades:
##    if 90<=Grades[i]<=100:
##        Grades[i]="A+"
##    elif 75<=Grades[i]<90:
##        Grades[i]="B-"
##    elif 60<=Grades[i]<75:
##        Grades[i]="C+"
##    elif 35<=Grades[i]<60:
##        Grades[i]="D-"
##    elif 10<=Grades[i]<35:
##        Grades[i]="E+"
##    else:
##        Grades[i]="F-"
##
##print(Grades)

##Account={}
##AN=None
##DA=None
##Amount=None
##AP=None
##print("Enter an Account Number")
##AN=int(input())
##print("Enter an Initial Deposit Amount")
##DA=int(input())
##if DA<0:
##    print("You're bankrupt")
##Account[AN]=DA
##print("Would you like to Withdraw or Deposit")
##AP=input()
##print("How much?")
##Amount=int(input())
##if AP=="Deposit":
##    Account[AN]=DA+Amount
##elif AP=="Withdraw":
##    Account[AN]=DA-Amount
##else:
##    print("Whaaa-?")
##if Account[AN]<0:
##    print("You're bankrupt and need",str(Amount-DA)+"$")
##else:
##    print("You have",str(Account[AN])+"$")

##Digits={1:"",2:"",3:"",
##        4:"",5:"",6:"",
##        7:"",8:"",9:""}
##for i in Digits:
##    print(i,end=": ")
##    if i%3==0:
##        print()
##for n in range(0,9,1):
##    print("Enter a Number")
##    Input=int(input())
##    if Input not in Digits:
##        print("Please Re-Enter a Number!")
##        Input=int(input())
##    if n%2==0:
##        Digits[Input]="X"
##    else:
##        Digits[Input]="O"
##
##    for i in Digits:
##        print(i,end=": "+Digits[i]+" ")
##        if i%3==0:
##            print()
##    if Digits[1]==Digits[2]==Digits[3]!="":
##        print(Digits[1],"Wins!")
##        break
##    if Digits[1]==Digits[5]==Digits[9]!="":
##        print(Digits[1],"Wins!")
##        break
##    if Digits[1]==Digits[4]==Digits[7]!="":
##        print(Digits[1],"Wins!")
##        break
##    if Digits[2]==Digits[5]==Digits[8]!="":
##        print(Digits[2],"Wins!")
##        break
##    if Digits[3]==Digits[6]==Digits[9]!="":
##        print(Digits[3],"Wins!")
##        break
##    if Digits[3]==Digits[5]==Digits[7]!="":
##        print(Digits[3],"Wins!")
##        break
##    if Digits[4]==Digits[5]==Digits[6]!="":
##        print(Digits[4],"Wins!")
##        break
##    if Digits[7]==Digits[8]==Digits[9]!="":
##        print(Digits[7],"Wins!")
##        break

##import pyautogui
##import time
##from keyboard import press
##from gtts import gTTS
##from audioplayer import AudioPlayer
##print("Would you like me to Search Up Something or Text Something?")
##Command=input()
##if Command=="Search":
##    print("Enter a Search")
##    Search=input()
##    print("Loading...")
##    time.sleep(1)
##    tts = gTTS(Search)
##    tts.save('/tmp/Searching Up'+Search+'... .mp3')
##    AudioPlayer('/tmp/Searching Up'+Search+'... .mp3').play(block=True)
##    pyautogui.click(20,129)
##    pyautogui.click(399,71)
##    time.sleep(0.2)
##    pyautogui.typewrite(Search)
##    press('enter')
##elif Command=="Text":
##    print("Enter a Text")
##    Text=input()
##    print("Loading...")
##    time.sleep(1)
##    tts = gTTS(Text)
##    tts.save('/tmp/Texting '+Text+'... .mp3')
##    AudioPlayer('/tmp/Texting '+Text+'... .mp3').play(block=True)
##    pyautogui.click(20,131)
##    pyautogui.click(399,71)
##    time.sleep(0.2)
##    pyautogui.typewrite("https://mail.google.com/mail/u/0/#inbox")
##    press('enter')
##    time.sleep(10)
##    pyautogui.click(170,904)
##    pyautogui.click(182,780)
##    time.sleep(7)
##    pyautogui.typewrite(Text)
    #press('enter')
   
##from keyboard import press
##print("Key?")
##Key=input()                             
##while True:
##    press(Key)

##import pyautogui
##while True:
##    print(pyautogui.position())

##characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
##a = {"hello" : characters}
##for i in characters:
##    print(characters[i])


##people={"Joe":25,"Jason":40,"Jackson":50, "James":45,"Jace":30,"Jones":35}
##oldest=[]
##for i in people:
##    oldest.append(people[i])
##age=max(oldest)
##print(age)
       
