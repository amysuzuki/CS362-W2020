# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:00:00 2020

@author: amysuzuk
"""
import Dominion

import testUtility as testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV, nC = testUtility.curseAndVictoryNum(player_names)

#Get Box
box = testUtility.getBox(nV)

#Get the supply order
supply_order = testUtility.getSupplyOrder()

#Get the supply
supply = testUtility.getSupply(player_names, box, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(["Annie","*Ben","*Carla", "*Sue", "Ron"])


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
