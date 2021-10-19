import random
def randomcard(card1 = random.randint(1, 100), card2 = random.randint(1, 100)):
    if card2 > card1:
        print('Too high!')
    if card2 < card1:
        print('Too Low!')
    if card2 == card1:
        print('Bingo!')
sum_player = 0
sum_computer = 0
z = 1
computer = 1
player = 1
while z < 4:
     player = int(input('insert a number between 1 to 100:  '))
     if player > 100:
         continue
     computer = random.randint(1, 100)
     randomcard(computer, player)
     if computer > player:
        sum_computer += 1
     if player > computer:
          sum_player += 1
     print('player score:', sum_player)
     print('computer score', sum_computer)
     z += 1

if sum_player > sum_computer:
    print('winner is the player with ', sum_player, ' score')
if sum_computer > sum_player:
    print('winner is the computer with ', sum_computer, ' score')


