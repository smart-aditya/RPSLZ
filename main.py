from random import *
from getpass import *
from time import *
print('It\'s very simple')
sleep(1)
print('Scissors cuts Paper')
sleep(1)
print('Paper covers Rock')
sleep(1)
print('Rock crushes Lizard')
sleep(1)
print('Lizard poisons Spock')
sleep(1)
print('Spock smashes Scissors')
sleep(1)
print('Scissors decapitates Lizard')
sleep(1)
print('Lizard eats Paper')
sleep(1)
print('Paper disproves Spock')
sleep(1)
print('Spock vaporizes Rock')
sleep(1)
print('(and as it always has) Rock crushes Scissors')
sleep(1)
print('\n'*120)
Actions={'rock':['','Smashes','Crushes',''],'paper':['Covers','','','Disproves'],'scissors':['','Cuts','Decapitates',''],'lizard':['','Eats','','Poisons'],'spock':['Vaporizes','','Smashes','']}
Moves=['rock','paper','scissors','lizard','spock']
WinTable=[[-1,1,0,0,4],[1,-1,2,3,1],[0,2,-1,2,4],[0,3,2,-1,3],[4,1,4,3,-1]]
Computer=0
x=input('Do you want to play against computer (y/n): ')
if x=='y':
  Computer=1
Name1=input('Player 1 enter your name: ')
Move1=getpass('%s enter your move: '%(Name1)).lower()
if Computer==0:
  Name2=input('Player 2 enter your name: ')
  Move2=getpass('%s enter your move: '%(Name2)).lower()
else:
  Name2='computer'
  Move2=Moves[randint(0,4)]
  print('Computer\'s Move:',Move2)
Index1=Moves.index(Move1)
Index2=Moves.index(Move2)
WinIndex=WinTable[Index1][Index2]
if WinIndex==-1 :
  print('IT IS A TIE')
else:
  if Index1==WinIndex:
    Moves.pop(Index1)
    a=Moves.index(Move2)
    print(Move1.upper(),Actions[Move1][a],Move2.upper())
    print(Name1.upper(),'WINS')
  else:
    Moves.pop(Index2)
    a=Moves.index(Move1)
    print(Move2.upper(),Actions[Move2][a],Move1.upper())
    print(Name2.upper(),'WINS')
