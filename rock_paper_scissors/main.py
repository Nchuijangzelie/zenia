#!/bin/python3

from random import randint
player = input('rock (r), paper (p) or scissors (s)?')
print(player, 'vs' , end=' ')

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
  computer = 'r'

elif chosen == 2:
  computer = 'p'
  
else:
  computer = 's'
  
print(computer)

#When you play what the computer has played it's a draw
if player == computer:
  print('DRAW!')
  
#when the player plays rock and the computer plays scissors the player wins
elif player == 'r' and computer == 's':
  print('Player wins!')
  
elif player == 'r' and computer == 'p':
  print('Computer wins!')

elif player == 'p' and computer == 'r':
  print('Player wins!')
  
elif player == 'p' and computer == 's':
  print('Computer wins!')
  
elif player == 's' and computer == 'r':
  print('Computer wins!')
  
elif player == 's' and computer == 'p':
  print('Player wins!')
  
else:
  print('ohohohoh')