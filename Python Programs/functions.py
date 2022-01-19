##def details():
##    print("Ronav, Age 9, 4'1 in height, black hair, brown eyes")
##
##for i in range(1,11,1):
##    details()


##import random
##def randomgen():
##    for i in range(1,6,1):
##        A=random.randint(1,20)
##        print(A)
##randomgen()


##def calc(a,x,y,z):                                    #Function Definition - A mini program that can be called several times within the main program.
##    sum=a+x+y+z
##    print(sum/4)
##
##calc(192837465,546372819,958473621,10110010100110)    #Function Call - To run and call the mini program within the main.




##def factorfinder(x):
##    for i in range(1,x+1,1):5
##        if x%i==0:
##            print(i)
##    
##while True:
##    print("Enter a Number")
##    Num=int(input())
##    factorfinder(Num)



##def TotalMoney(Tax, Price):
##    TaxCalc=Tax/100
##    Total=TaxCalc+Price
##    print(Total)
##TotalMoney(5,10)


##def TotalMoney(Tax, Price):
##    TaxCalc=Tax/100
##    Total=TaxCalc+Price
##    return Total
##Func=TotalMoney(5,10)
##print(Func)


##def Total(Q,D,N,P):
##    print(Q+D+N+P)
##
##def Quarter(x):
##    Q=x*0.25
##    return Q
##def Dime(y):
##    D=y*0.10
##    return D
##def Nickel(z):
##    N=z*0.05
##    return N
##def Penny(a):
##    P=a*0.01
##    return P
##print("Enter an amount of Quarters ")
##x=int(input())
##print("Enter an amount of Dimes")
##y=int(input())
##print("Enter an amount of Nickels")
##z=int(input())
##print("Enter an amount of Pennies")
##a=int(input())
##Q1=Quarter(x)
##D1=Dime(y)
##N1=Nickel(z)
##P1=Penny(a)
##Total(Q1,D1,N1,P1)


##def Alphabet(Word):
##    Letters=list(Word)
##    Letters.sort(reverse=1)
##    String="".join(Letters)
##    return String
##print("ENTER A WORD NOW!")
##Input=input()
##String1=Alphabet(Input)
##print(String1)

##def animals(Input):
##    Wild=("Tiger","Lion","Wolf", "Monkey", "Elephant")
##    Domestic=("Cat", "Dog", "Hamsters", "Guinea Pigs", "Fish")
##    if Input in Wild:
##        print("A",Input,"is a wild animal")
##    if Input in Domestic:
##        print("A",Input,"is a domestic animal")
##print("Name an Animal")
##Input=input()
##animals(Input)


##def Rect(Length, Width):
##    Rect_Area=Length*Width
##    return Rect_Area
##def Tri(Height, Base):
##    Tri_Area=0.5*Base*Height
##    return Tri_Area
##def Circle(Radius):
##    Circle_Area=3.14*Radius**2
##    return Circle_Area



##a=5
##def PlusFive():
##    global a
##    a+=5
##    print(a)
##
##PlusFive()
##PlusFive()
##PlusFive()


##print("Enter an Acc Number")
##Acc=int(input())
##print("Enter an Amount")
##Num=int(input())
##print("Would you like to Withdraw or Deposit?")
##Operation=input()
##AccNum={1234:4321,4321:1234,1324:4231,4231:1324}
##def Value(AccountNumber, Deposit, Operation):
##    if Operation=="Deposit":
##        AccNum[AccountNumber]=Num+AccNum[AccountNumber]
##        print(AccNum[AccountNumber])
##    if Operation=="Withdraw":
##        AccNum[AccountNumber]=AccNum[AccountNumber]-Num
##        print(AccNum[AccountNumber])
##Value(Acc,Num,Operation)


##def Array(Rows=10,Columns=10):
##    for i in range(1,Rows+1,1):
##        print()
##        for i in range(1,Columns+1,1):
##            print("*",end=" ")
##Array()





























