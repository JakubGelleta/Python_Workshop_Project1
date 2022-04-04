import random

def get_number():
    '''
    This function checks if the user input is correct,
    in case of wrong input it returns text information about error.
    :return:
    '''
    while True:
        try:
            result = int(input("Guess the number in range from 1 to 100: "))
            break
        except ValueError:
            print("It's not a number...")

    return result


def guess_number():
    '''
    Main function of the game:
    It's comparing user input number and computer draw number,
    and in each case returns appropriate information.
    :return:
    '''
    computer_number = random.randint(1, 100)
    user_number = get_number()

    while computer_number != user_number:
        if computer_number > user_number:
            print("Too small!")
        else:
            print("Too big!")

        user_number = get_number()
    print("You won !")

if __name__ == '__main__':
    guess_number()