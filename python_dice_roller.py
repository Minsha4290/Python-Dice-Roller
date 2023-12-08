import random as rd
print('hey, I am a dice what do you want me to do')

FEATURE = int(input('the features i offer are \n 1. One Die \n 2. Two Dice \n 3. Three Dice \n 4. Custom Number of Dice with custom number of faces \n'))

def one_die():
    ROLL = rd.randint(1,6)
    print('You got a ', ROLL)


def two_dice():
    ROLL1 = rd.randint(1,6)
    ROLL2 = rd.randint(1,7)
    print('You got a', ROLL1, ROLL2)
    
def three_dice():
    ROLL1 = rd.randint(1,6)
    ROLL2 = rd.randint(1,6)
    ROLL3 = rd.randint(1,6)
    print('You got a', ROLL1, ROLL2, ROLL3)

def custom_dice():
    FACES = int(input('Enter the number of faces: '))
    NUMBER_DICES = int(input('Enter the number of dice: '))
    ROLLS = []
    for _ in range(NUMBER_DICES):
        ROLLS.append(rd.randint(1, FACES))
    rolls_as_string = ', '.join(map(str, ROLLS))
    print(rolls_as_string)

    


if FEATURE == 1:
    one_die()

if FEATURE == 2:
    two_dice()

if FEATURE == 3:
    three_dice()
    
if FEATURE == 4:
    custom_dice()
