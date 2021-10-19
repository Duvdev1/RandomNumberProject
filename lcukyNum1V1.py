import random
import time
def randomcard(card1 = random.randint(1, 100), card2 = random.randint(1, 100)):
    break1 = 0
    if card2 > card1:
        print('Too high!')
    if card2 < card1:
        print('Too Low!')
    if card2 == card1:
        print('Bingo!')
computer = 1
player = 0
while computer != player:
    player = int(input('insert a number:  '))
    computer = random.randint(1, 100)
    randomcard(computer, player)

