import random
import time
from collections import Counter

done = 'false'
#here is the animation
def animate():
    Count=0
    global done
    print('loading… |',end="")
    while done == 'false':
        time.sleep(0.1)
        print('/',end="")
        time.sleep(0.1)
        print('-',end="")
        time.sleep(0.1)
        print('\\',end="")
        time.sleep(0.1)
        Count+=1
        if Count==10:
            done='true'
    print()
    print('Done!')
    

animate()
done = 'false'

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
Stats={}

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


def Is_Straight(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort()
  if Card_Value[0]+1==Card_Value[1] and Card_Value[1]+1==Card_Value[2] and Card_Value[2]+1==Card_Value[3] and Card_Value[3]+1==Card_Value[4]:
    return True
  elif Card_Value[4] in Aces:
      if Card_Value[4]-12==Card_Value[0] and Card_Value[0]+1==Card_Value[1] and Card_Value[1]+1==Card_Value[2] and Card_Value[2]+1==Card_Value[3]:
        return True
      else:
        return False
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

def Get_MRC(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Values=list(Counter(Card_Value).values())
  Keys=list(Counter(Card_Value).keys())
  Max_Value_Index=Values.index(max(Values))
  return Keys[Max_Value_Index]

#GET Top Two Repeat Cards
def Get_TTRC(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Values=list(Counter(Card_Value).values())
  Keys=list(Counter(Card_Value).keys())
  if 1 in Values:
      Min_Value_Index=Values.index(1)
      Keys.pop(Min_Value_Index)
  return Keys

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
  return not Is_Three_of_a_Kind(Cards) and len(Counter(Card_Value).keys())==3

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
  
def Play(Name):
  Result=10
  Cards=Draw_Five()
  #Cards=[0,13,2,15,25]
  print("Drawing Cards for",Name+"…")
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
    print("You got a Four of a Kind of",Card_Deck[Get_MRC(Cards)-1],"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Full_House(Cards):
    Result=4
    RepeatCards=[]
    for dv in Get_TTRC(Cards):
        RepeatCards.append(Card_Deck[dv-1])
    print("You got a Full House",RepeatCards,"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Flush(Cards):
    Result=5
    print("You got a Flush and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Straight(Cards):
    Result=6
    print("You got a Straight and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Three_of_a_Kind(Cards):
    Result=7
    print("You got a Three of a Kind of",Card_Deck[Get_MRC(Cards)-1],"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_Two_Pair(Cards):
    Result=8
    RepeatCards=[]
    for dv in Get_TTRC(Cards):
        RepeatCards.append(Card_Deck[dv-1])
    print("You got Two Pairs",RepeatCards,"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  elif Is_One_Pair(Cards):
    Result=9
    print("You got a Pair of",Card_Deck[Get_MRC(Cards)-1],"and your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  else:
    print("You got a High Card!", Card_Deck[Get_High_Card(Cards)-1])

  #print("Your Highest Card is",Card_Deck[Get_High_Card(Cards)-1])
  Result_Array=[Get_High_Card(Cards),Get_2nd_High_Card(Cards),Get_3rd_High_Card(Cards),Get_4th_High_Card(Cards),Get_5th_High_Card(Cards)]
  return Cards,Result,Result_Array,Get_MRC(Cards)


def declare_winner(P1_Name,P1_Score,P2_Name,P2_Score):
  if P1_Score>P2_Score:
    Stats[P1_Name]+=1
    print(P1_Name,"Wins!")
  elif P1_Score<P2_Score:
    Stats[P2_Name]+=1
    print(P2_Name,"Wins!")

    
def breaktie(P1_Name,P1_Result_Array,P2_Name,P2_Result_Array,idx):
  if P1_Result_Array[idx]==P2_Result_Array[idx]:
    if idx==4:
      Stats[P2]+=0.5
      Stats[P1]+=0.5
      print(P1_Name,"and",P2_Name,"have tied. It's a draw!")
    else:
      breaktie(P1_Name,P1_Result_Array,P2_Name,P2_Result_Array,idx+1)
  else:
    declare_winner(P1_Name,P1_Result_Array[idx],P2_Name,P2_Result_Array[idx])

def Check_High_Card(P1,P1_Result_Array,P2,P2_Result_Array):
    if P1_Result_Array[0]==P2_Result_Array[0]:
        breaktie(P1,P1_Result_Array,P2,P2_Result_Array,1)
    else:
        declare_winner(P1,P1_Result_Array[0],P2,P2_Result_Array[0])

def Start_Game(P1,P2,Game_Number):
  print("______________________________________________")
  input(P1 + ", Hit Enter when Ready ")
  (P1_Cards,P1_Result,P1_Result_Array,P1_MRC)=Play(P1)
  for i in range(1,3,1):
    print()
  input(P2 + ", Hit Enter when Ready ")
  (P2_Cards,P2_Result,P2_Result_Array,P2_MRC)=Play(P2)
  for i in range(1,3,1):
    print()
  #comparing results to find a winner
  if P1_Result==P2_Result:
    if P1_Result in [3,4,7,9]:
        if P1_MRC>P2_MRC:
            Stats[P1]+=1
            print(P1,"Wins!")
        elif P1_MRC<P2_MRC:
            Stats[P2]+=1
            print(P2,"Wins!")
        else:
            Check_High_Card(P1,P1_Result_Array,P2,P2_Result_Array)
    elif P1_Result==8:
        #both players have 2 pairs
        P1_TTRC=Get_TTRC(P1_Cards)
        P2_TTRC=Get_TTRC(P2_Cards)
        if P1_TTRC[0]>P2_TTRC[0] and P1_TTRC[0]>P2_TTRC[1]:
            Stats[P1]+=1
            print(P1,"Wins!")
        elif P1_TTRC[1]>P2_TTRC[0] and P1_TTRC[0]>P2_TTRC[1]:
            Stats[P1]+=1
            print(P1,"Wins!")
        elif P2_TTRC[0]>P1_TTRC[0] and P2_TTRC[0]>P1_TTRC[1]:
            Stats[P2]+=1
            print(P2,"Wins!")
        elif P2_TTRC[1]>P1_TTRC[0] and P2_TTRC[0]>P1_TTRC[1]:
            Stats[P2]+=1
            print(P2,"Wins!")
        else:
            Check_High_Card(P1,P1_Result_Array,P2,P2_Result_Array)
    else:
        Check_High_Card(P1,P1_Result_Array,P2,P2_Result_Array)        
  elif P1_Result>P2_Result:
    Stats[P2]+=1
    print(P2,"Wins!")
  elif P1_Result<P2_Result:
    Stats[P1]+=1
    print(P1,"Wins!")
  print("Current Stats:",Stats)
  print("______________________________________________")
  Continue=input("Would You Like to Play Again? ")
  if "n" not in Continue and "N" not in Continue:
    print("Ok, Starting Game",Game_Number+1)
    if len(Used_Cards)>42:
      print("Our Virtual Deck has ran out of cards. Shuffling…")
      time.sleep(1.5)
      print("Deck Incoming!")
      Used_Cards.clear()
    Start_Game(P1,P2,Game_Number+1)
  else:
    print("Thank You for Playing Poker Online: Multiplayer (Single Deck Edition)!")

print("Welcome To Poker Online: Multiplayer (Single Deck Edition)!")    
print()
P1=input("Player 1, Please Enter Your Name: ")
P2=input("Player 2, Please Enter Your Name: ")
Stats[P1]=0
Stats[P2]=0
Start_Game(P1,P2,1)
