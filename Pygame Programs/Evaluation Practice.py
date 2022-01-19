##print("Enter a Number")
##num1=int(input())
##print("Enter a Number")
##num2=int(input())
##print("Enter an Operator")
##operation=input()
##if operation=="+":
##    print(int(num1+num2))
##elif operation=="–":
##    print(int(num1-num2))
##elif operation=="x":
##    print(int(num1*num2))
##elif operation=="÷":
##    if num2==0:
##        print("∞")
##    else:
##        print(int(num1/num2))
##else:
##    print("Invalid Operator")

##numbers=[]
##for i in range(1,51,1):
##    if i%5==0:
##        numbers.append(i)
##print(numbers)


##print("Enter a Number")
##stop=int(input())
##counter=0
##while counter!=stop:
##    counter+=1
##    print(counter)


##for i in range(1,4,1):
##    print()
##    for i in range(1,5,1):
##        print("?",end=" ")


##while True:
##    print("Enter a Color")
##    color=input()
##    if color=="black" or color=="Black":
##        break
##    print(color)


##names=["John","Jack","Kim","Brad","Jacob"]
##names.append("Ryan")
##print(names)
##print(names[1:])
##names[2]="Mike"
##print(names)
##names.insert(1,"Alice")
##print(names)
##names.remove("Jacob")
##print(names)
##names.pop(0)
##print(names)
##names.sort(reverse=1)
##print(names)


##import random
##numbers=[]
##counter=1
##while counter<=10:
##    num=random.randint(1,10)
##    if num not in numbers:
##        numbers.append(num)
##        counter+=1
##print(numbers)


##animals={'cat':3,'dog':5,'parrot':2}
##animals['tigers']=7
##print(animals)
##animals['cat']=2
##print(animals)



##people={'Joe':23,'Tom':18,'Jerry':17}
##print("Enter a Name")
##name1=input()##print("Enter their Age")
##age=int(input())
##people[name1]=age
##print(people)
##print("Enter a user's name")
##name2=input()
##if name2 in people:
##    print(people[name2])
##else:
##    print("Unidentified Username")


##car={"brand":"Ford","model":"Mustang","year":1964}
##print(car)
##car["year"]=2018
##print(car)


##print("a",ord('a'))
##print("z",ord('z'))
##alpha={}
##for i in range(97,122,1):
##    alpha[chr(i)]=i
##print(alpha)


##letters=[]
##counter=0
##print("Enter a Word")
##word=input()
##letters=list(word)
##print(letters)
##alpha={}
##alphabet={}
##for i in range (97,122,1):
##    counter+=1
##    alphabet[chr(i)]=counter
##for w in letters:
##    alpha[w]=alphabet[w]
##print(alpha)


##import random
##Names={"John":"","Gerald":"","Ronav":"","Anoop":"","Ally":""}
##for n in Names:
##    name=list(n.lower())
##    for c in name:
##        if c in ["a","e","i","o","u"]:
##            name.remove(c)
##    random.shuffle(name)
##    answer="".join(name)
##    Names[n]=answer
##print(Names)


##names=["jack","john","alice","maria","kim"]
##initials=[]
##for n in names:
##    initials.append(n[0])
##answer="".join(initials)
##print(answer)




























































