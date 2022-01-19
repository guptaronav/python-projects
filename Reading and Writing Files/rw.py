##filevar = open("Paragraph.txt","r")
##fileread=filevar.read()
##print(fileread)
##filevar.close()


##import pyautogui
##from keyboard import press
##import keyboard
##import time
##newline="\n"
##filevarw=open("spam.txt","w")
##print("Enter a Command")
##textvar=input()
##filevarw.write(textvar+newline)
##if textvar=="/spam":
##    print("Enter what You'd Spam Please.")
##    spam=input()
##    time.sleep(0.5)
##    print("Loading, Please Beware of the Spam in 3, 2, 1...")
##    time.sleep(1)
##    print("Incoming Spam Attack!!!")
##    time.sleep(0.5)
##    while True:
##        pyautogui.typewrite(spam)
##        press('enter')
##        if keyboard.is_pressed('q'):
##            break
##            pyautogui.click(1127,279)
##else:
##    print("Invalid Command; Please Try Again.")
##filevarw.write("")
##filevarw.close()
##filevarr=open("spam.txt","r")
##filereadr=filevarr.read()
##print(filereadr)
##filevarr.close()


##Run when Cursor Her to Prevent Spam Ending Delay Interference; Spam Trash Can Here:        Click Here: 


##filevar=open("hobbies.txt","w")
##filevar.write("I like coding. Coding is a hobby! \n")
##filevar.write("Coding is fun, but complex. Hobbies are entertaining activities for people to do or play. \n")
##filevar.write("Coding has a varieties of modules and packages for everyone, it allows you to do ANYTHING! Just code it!!!")
##filevar.close()

##filevar=open("hobbies.txt","a")
##filevar.write("I hate coding. Coding is not a hobby! \n")
##filevar.write("Coding is boring, but easy. Hobbies aren't entertaining activities for people to do or play. \n")
##filevar.close()

##print("Enter a String!")
##String=input()
##print(String.upper())
##print(String.lower())


##import random
##total=0
##filevar=open("randomintegers.txt", "w")
##for i in range(1,1001):
##    A=random.randint(1,1000)
##    filevar.write(str(A)+"\n")
##filevar.close()
##fileread=open("randomintegers.txt","r")
##for n in fileread:
##    n=n.strip()
##    print(n)
##    total=total+int(n)
##print("The sum of the 1000 =",total)
##fileread.close()



##filewrite=open("Source.txt","w")
##filewrite.write("Barney Rubble \n Jason McKraken \n Jessie July \n Mary Dune \n Jackson Grey \n")
##filewrite.close()
##fileread=open("Source.txt","r")
##for i in fileread:
##    Name=i.split()
##    print(Name[0][0:3],Name[1])
##fileread.close()



##filewrite=open("Source.txt","w")
##print("Enter Your Full Name Please")
##Name=input()
##filewrite.write(Name+"\n")
##filewrite.close()
##fileread=open("Source.txt","r")
##for i in fileread:
##    Username=i.split()
##    print(Username[0][0:3],Username[1])
##fileread.close()

##varlist=[]
##fileread=open("wordlist.txt","r")
##for filedata in fileread:
##    filedata=filedata.strip()
##    varlist.append(filedata)
##print(len(varlist))


##varlist={}
##fileread=open("wordlist.txt","r")
##for filedata in fileread:
##    filedata=filedata.strip()
##    if filedata[0]=="a":
##     varlist.append(filedata[0])
##print(len(varlist))




##x=""
##i=0
##answer=[]
##print("Enter a String")
##string=input()
##tup=tuple(string.lower())
##size=len(tup)
##while i<size:
##    if tup.count(tup[i])<=1:
##        answer.append(tup[i]) 
##    i+=1 
##print(x.join(answer))



##import random
##num=random.randint(10,50)
##filevar=open("name.txt","w")
##print("enter a name")
##name=input()
##filevar.write(name)
##filevar.write(str(num))
##filevar.close()
##filevar=open("name.txt","r")
##fileread=filevar.read()
##print(fileread)



##palindrome=open("palindrome.txt","w")
##print("Enter a String")
##string=input()
##palindrome.write(string)
##if string==string[::-1]:
##    palindrome.write("true")
##else:
##    palindrome.write("false")
##palindrome.close()
##testread=open("palindrome.txt","r")
##read=testread.read()
##print("Palindrome:",read)


##text=open("alphanumeric.txt","w")
##print("Enter a String")
##string=input()
##text.write(string+"\n")
##if string.isalnum():
##    text.write("true")
##else:
##    text.write("false")
##text.close()
##textread=open("alphanumeric.txt","r")
##read=textread.read()
##print(read)

##answer=[]
##x=""
##vowels=["a","e","i","o","u"]
##vowel=open("vowels.txt","w")
##print("enter a string")
##string=input()
##vowel.write(string)
##letters=list(string)
##for c in letters:
##    if c in vowels:
##        answer.append(c)
##vowelcount=x.join(answer)
##print(len(vowelcount))


##x=""
##i=0
##answer=[]
##print("Enter a String")
##string=input()
##tup=tuple(string.lower())
##size=len(tup)
##while i<size:
##    if tup.count(tup[i])<=1:
##        answer.append(tup[i]) 
##    i+=1 
##print(x.join(answer))

##answer=[]
##x=""
##print("enter a string")
##string=input()
##letters=list(string)
##for c in letters:
##    if c not in answer: 
##        answer.append(c)    
##text=x.join(answer)
##print(text)

##num=0
##wordfile=open("wordlist.txt","r")
##for c in wordfile:
##    c=c.strip()
##    if c[-1] == "y":
##        print(c)
##        num+=1
##print(num)





##num=0
##numlist=[]
##filevar=open("wordlist.txt","r")
##dictionary={}
##for c in filevar:
##    if c[0] in dictionary:
##        dictionary[c[0]]+=1
##    else:
##        dictionary[c[0]]=1
##print(dictionary)
##for i in dictionary:
##    numlist.append(dictionary[i])
##numlist.sort(reverse=1)
##print(numlist)
##ans=numlist[0]
##for key,value in dictionary.items():
##    if value==ans:
##        print("Answer is",key,value)



##print("Enter a Letter")
##let1=input()
##print("Enter a Letter")
##let2=input()
##print("Enter a Letter")
##let3=input()
##filevar=open("wordlist.txt","r")
##for w in filevar:
##    w=w.strip()
##    if let1 in w and let2 in w and let3 in w:
##        print(w)
##filevar.close()





##filevar=open("wordlist.txt","r")
##for w in filevar:
##    w=w.strip()
##    if w==w[::-1]:
##        print(w)
    




##filevar=open("names.txt","w")
##filevar.write("Joe \n")
##filevar.write("Carl \n")
##filevar.write("Kai \n")
##filevar.write("John \n")
##filevar.write("Jerry \n")
##filevar.close()
##fileadd=open("names.txt","a")
##fileadd.write("Johnson \n")
##fileadd.write("Karlson")
##fileadd.close()
##fileread=open("names.txt","r")
##read=fileread.read()
##print(read)
##fileread.close()
##



##import random
##counter=0
##file=open("numbers.txt","w")
##numbers=[]
##for i in range(1,501,1):
##    a=random.randint(1,1000)
##    file.write(str(a)+"\n")
##    counter+=a
##file.close()
##fileread=open("numbers.txt","r")
##var=fileread.read()
##fileread.close()
##print(var)
##print("Sum =",counter)


##words=[]
##filevar=open("wordlist.txt","r")
##for w in filevar:
##    w=w.strip()
##    if w[0]=="a" and w[-1]=="s":
##        words.append(w)
##print(words)



##import random
##counter=0
##add=0
##prod=1
##filevar=open("random_integers.txt","w")
##for i in range(1,11,1):
##    a=random.randint(1,100)
##    filevar.write(str(a)+"\n")
##filevar.close()
##fileread=open("random_integers.txt","r")
##for w in fileread:
##    w=w.strip()
##    counter+=1
##    print(w)
##    if counter<=5:
##        add+=int(w)
##    else:
##        prod=prod*int(w)
##print("Sum =",add,"Product =",prod)
##fileread.close()








































































