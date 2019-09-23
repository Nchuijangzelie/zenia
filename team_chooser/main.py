#!/bin/python3
from random import choice
#this code below creats a list from player.txt file
#players = ['Zelie','Ashley','Rodrigue','Sebastien','Kcenia','Susan','Julius','Amin']
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print(players)

#this code creates three empty list
teamA = []
teamB = []
teamC = []

#this code shows that while loop is added to keep choosing players until the lengh of the player list is zero
while len(players) > 0:
  playerA = choice(players)
  #print(playerA)
  teamA.append(playerA)
  players.remove(playerA)
  #print('Players left:', players)

#this code shows that ifall players are chosen then stop
  if players == []:
    break
#this code is to chose playerB. 
  playerB = choice(players)
  #print (playerB)
  teamB.append(playerB)
  players.remove(playerB)

#this code shows that ifall players are chosen then stop
  if players == []:
    break

#this code is to chose playerC.   
  playerC = choice(players)
  #print (playerC)
  teamC.append(playerC)
  players.remove(playerC)
  #print('players left:',players)


#this code below creats a list from Zelie.txt file
teamNames = []
file = open('Zelie.txt', 'r')
teamNames = file.read().splitlines()

#the code below give your teams random names for the three teams
teamNamesA = choice(teamNames)
teamNames.remove(teamNamesA)
teamNamesB = choice(teamNames) 
teamNames.remove(teamNamesB)
teamNamesC = choice(teamNames)
teamNames.remove(teamNamesC)

#the code below print team names 
print('This are your teams')
print(teamNamesA ,teamA)
print(teamNamesB ,teamB)
print(teamNamesC ,teamC)
