def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def welcome():
    return 'Welcome to Number Guess'



import random
def game_():
    user_response = input("Please input a number between 0 and 100:")
    try:
        val = int(user_response)
    except ValueError:
        print("This is not a valid integer. Please try again")
        game_()
    if val < num:
        print("Wrong Guess: This is lower than actual number.")
    elif val > num:
        print("Wrong Guess: This is higher than actual number")
    else:
        print("This is the correct number")



def Replay():
    ans = input('Do you want to play again? [Y/N]: ')
    if ans == 'Y'or ans == 'y':
        game_()
    else:
        exit()

if __name__=="__main__":
    num = random.randrange(0, 100)
    print(welcome())
    game_()
    Replay()




