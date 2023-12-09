import random as rd

def one_die():
    ROLL = rd.randint(1, 6)
    print('You got a', ROLL)

def two_dice():
    ROLL1 = rd.randint(1, 6)
    ROLL2 = rd.randint(1, 7)
    print('You got a', ROLL1, ROLL2)

def three_dice():
    ROLL1 = rd.randint(1, 6)
    ROLL2 = rd.randint(1, 6)
    ROLL3 = rd.randint(1, 6)
    print('You got a', ROLL1, ROLL2, ROLL3)

def custom_dice():
    FACES = int(input('Enter the number of faces: '))
    NUMBER_DICES = int(input('Enter the number of dice: '))
    ROLLS = [rd.randint(1, FACES) for _ in range(NUMBER_DICES)]
    rolls_as_string = ', '.join(map(str, ROLLS))
    print('You got:', rolls_as_string)

def main():
    while True:
        print('\nHey, I am a dice. What do you want me to do?')
        FEATURE = int(input('The features I offer are:'
                            '\n1. One Die'
                            '\n2. Two Dice'
                            '\n3. Three Dice'
                            '\n4. Custom Number of Dice with custom number of faces'
                            '\n5. Quit\n'))

        if FEATURE == 1:
            one_die()
        elif FEATURE == 2:
            two_dice()
        elif FEATURE == 3:
            three_dice()
        elif FEATURE == 4:
            custom_dice()
        elif FEATURE == 5:
            print('Goodbye!')
            break
        else:
            print('Invalid option. Please choose a valid option.')

        play_again = input('Do you want to try again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Goodbye!')
            break

main()
