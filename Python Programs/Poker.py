# -*- coding: iso-8859-15 -*-
import random
import time
from collections import Counter
Card_Deck=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
Suits=['♠','♣︎','♥︎','♦']
Deck=['2 ♠','3 ♠','4 ♠','5 ♠','6 ♠','7 ♠','8 ♠','9 ♠','10 ♠','J ♠','Q ♠','K ♠','A ♠',
      '2 ♣︎','3 ♣︎','4 ♣︎','5 ♣︎','6 ♣︎','7 ♣︎','8 ♣︎','9 ♣︎','10 ♣︎','J ♣︎','Q ♣︎','K ♣︎','A ♣︎',
      '2 ♥︎','3 ♥︎','4 ♥︎︎','5 ♥︎','6 ♥︎','7 ♥︎︎','8 ︎♥︎','9 ♥︎︎','10 ♥︎','J ♥︎','Q ♥︎','K ♥︎','A ♥︎',
      '2 ♦︎','3 ♦︎','4 ♦︎︎','5 ♦︎','6 ♦︎','7 ♦︎︎','8 ︎♦','9 ♦','10 ♦︎','J ♦︎','Q ♦','K ♦','A ♦']
Deck_Value=[1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13]
Spades=[0,1,2,3,4,5,6,7,8,9,10,11,12]
Clubs=[13,14,15,16,17,18,19,20,21,22,23,24,25]
Hearts=[26,27,28,29,30,31,32,33,34,35,36,37,38]
Diamonds=[39,40,41,42,43,44,45,46,47,48,49,50,51]
Aces=[12,25,38,51]
Used_Cards=[]


def deal():
  A=random.randint(0,51)
  if A not in Used_Cards:
    Used_Cards.append(A)
    return A
  else:
    return deal()
  
def Draw_Five():
  A=deal()
  B=deal()
  C=deal()
  D=deal()
  E=deal()
  Cards_in_Hand=[A,B,C,D,E]
  return Cards_in_Hand

def Compare(A,B):
  if Deck_Value[A]>Deck_Value[B]:
    return 1
  elif Deck_Value[A]<Deck_Value[B]:
    return -1
  else:
    return 0


##Card_1=deal()
##Card_2=deal()
##print(Card_1,Card_2)
##Result=Compare(Card_1,Card_2)
##if Result==0:
##  print(Deck[Card_1],"is equal to",Deck[Card_2])
##elif Result==1:
##  print(Deck[Card_1],"is greater than",Deck[Card_2])
##elif Result==-1:
##  print(Deck[Card_1],"is less than",Deck[Card_2])


def Is_Straight(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort()
  if Card_Value[0]+1==Card_Value[1] and Card_Value[1]+1==Card_Value[2] and Card_Value[2]+1==Card_Value[3] and Card_Value[3]+1==Card_Value[4]:
    return True
  else:
    return False

def Print_Cards(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck[i])
  print(Card_Value)

def Is_Flush(Cards):
  return all(item in Spades for item in Cards) or all(item in Clubs for item in Cards) or all(item in Hearts for item in Cards) or all(item in Diamonds for item in Cards)
  
def Is_Straight_Flush(Cards):
  return Is_Straight(Cards) and Is_Flush(Cards)

def Is_Royal_Flush(Cards):
  Cards.sort(reverse=1)
  return Cards[0] in Aces and Is_Straight_Flush(Cards)

def OAK(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return max(Counter(Card_Value).values())

def Get_Max_Repeat_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Values=list(Counter(Card_Value).values())
  Keys=list(Counter(Card_Value).keys())
  Max_Value_Index=Values.index(max(Values))
  return Keys[Max_Value_Index]

def Is_Four_of_a_Kind(Cards):
  return OAK(Cards)==4

def Is_Three_of_a_Kind(Cards):
  return OAK(Cards)==3

def Is_One_Pair(Cards):
  return OAK(Cards)==2

def Is_Two_Pair(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return len(Counter(Card_Value).keys())==3

def Is_Full_House(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return len(Counter(Card_Value).keys())==2 and Is_Three_of_a_Kind(Cards)

def Get_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[0]

def Get_2nd_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[1]

def Get_3rd_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[2]

def Get_4th_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[3]

def Get_5th_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[4]
  
def Play():
  Result=10
  Cards=Draw_Five()
  print("Drawing Cards…")
  time.sleep(2.5)
  Print_Cards(Cards)
  if Is_Royal_Flush(Cards):
    Result=1
    print("You got a Royal Flush and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Straight_Flush(Cards):
    Result=2
    print("You got a Straight Flush and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Four_of_a_Kind(Cards):
    Result=3
    print("You got a Four of a Kind of",Card_Deck[Get_Max_Repeat_Card(Cards)-1],"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Full_House(Cards):
    Result=4
    print("You got a Full House and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Flush(Cards):
    Result=5
    print("You got a Flush and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Straight(Cards):
    Result=6
    print("You got a Straight and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Three_of_a_Kind(Cards):
    Result=7
    print("You got a Three of a Kind of",Card_Deck[Get_Max_Repeat_Card(Cards)-1],"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Two_Pair(Cards):
    Result=8
    print("You got Two Pairs and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_One_Pair(Cards):
    Result=9
    print("You got a Pair of",Card_Deck[Get_Max_Repeat_Card(Cards)-1])
  else:
    print("You got a High Card!", Card_Deck[Get_High_Card(Cards)-1])

  #print("Your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  return Result,Get_High_Card(Cards),Get_2nd_High_Card(Cards),Get_3rd_High_Card(Cards),Get_4th_High_Card(Cards),Get_5th_High_Card(Cards)

print("Player 1, Welcome To Poker Online, Please Enter Your Name")
P1=input()
print(P1,"Hit Enter when Ready")
input()
(P1_Results, P1_HC, P1_2H,P1_3H,P1_4H,P1_5H)=Play()
for i in range(1,4,1):
  print()
print("Player 2, Please Enter Your Name")
P2=input()
print(P2,"Hit Enter when Ready")
input()
(P2_Results, P2_HC,P2_2H,P2_3H,P2_4H,P2_5H)=Play()
for i in range(1,4,1):
  print()
if P1_Results==P2_Results:
  if P1_HC>P2_HC:
    print(P1,"Wins!")
  elif P1_HC<P2_HC:
    print(P2,"Wins!")
  else:
    print(P1,"and",P2,"have tied.")
elif P1_Results>P2_Results:
  print(P2,"Wins!")
elif P1_Results<P2_Results:
  print(P1,"Wins!")