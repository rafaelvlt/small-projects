import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname) s- %(message)s')
logging nao deve aparecer para o usuario


guess = ""
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess is ' + guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'
logging.debug('Toss is: ' + str(toss))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == 1:
        toss = 'heads'
    else:
        toss = 'tails'
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
