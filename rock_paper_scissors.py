# Rock, Paper, Scissors Game
import random

print('================================')
print("Rock Paper Scissors Lizard Spock")
print('================================')
print()
print('1)', '✊')
print('2)', '✋')      
print('3)', '✌️')
print('4)', '🦎')
print('5)', '🖖')
player = int(input('Pick a number: '))
computer = random.randint(1, 5)
print()

while player < 1 or player > 5:
    print("Invalid choice. Please choose a number between 1 and 5.")
    player = int(input('Pick a number: '))
    
# Convert numbers to symbols
#Computer's choice
if computer == 1:
    computer = '✊'
elif computer == 2:
    computer = '✋'
elif computer == 3:
    computer = '✌️'
elif computer == 4:
    computer = '🦎'
elif computer == 5:
    computer = '🖖'
## Player's choice
if player == 1:
    player = '✊'
elif player == 2:
    player = '✋'
elif player == 3:
    player = '✌️'
elif player == 4:
    player = '🦎'
elif player == 5:
    player = '🖖'

print(f'YOU chose: {player}')
print(f'CPU chose: {computer}')
if player == computer:
    print("It's a tie!")
elif (player == '✊' and (computer == '✌️' or computer == '🦎')) or \
    (player == '✋' and (computer == '✊' or computer == '🖖')) or \
    (player == '✌️' and (computer == '✋' or computer == '🦎')) or \
    (player == '🦎' and (computer == '🖖' or computer == '✋')) or \
    (player == '🖖' and (computer == '✊' or computer == '✌️')):
    print("You win!")
else:
    print("You lose!")