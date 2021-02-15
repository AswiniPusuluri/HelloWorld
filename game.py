import random

'''Game Rules
    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissor'''

def player():
    mylist = ['R', 'P', 'S', 'L', 'V']
    while True:
        user_input = input('Enter your choice in Capital Letters:')
        if user_input not in mylist:
            print("Please enter valid input")
            continue
        if user_input in mylist:
            return user_input


def computer():
    comp_choice = random.choice(['R','P','S','L','V'])
    return comp_choice

def game():
    mydict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissor', 'L': 'Lizard', 'V': 'Spock'}
    player_choice = player()
    choice_name = mydict[player_choice]
    print("players choice is:"+choice_name)
    comp_choice = computer()
    comp_choice_name = mydict[comp_choice]
    print("computer choice is:"+comp_choice_name)
    print(choice_name+"V/s"+comp_choice_name)
    final_result = ''
    if comp_choice_name == choice_name:
        print("It's a TIE => So reselect")
        game()

    if ((choice_name=='Paper' and comp_choice_name=='Scissor')or(choice_name=='Scissor'and comp_choice_name=='Paper')):
        print("Scissor Wins")
        final_result = "Scissor"
    elif ((choice_name=='Paper' and comp_choice_name=='Rock')or(choice_name=='Rock'and comp_choice_name=='Paper')):
        print("Paper Wins")
        final_result = "Paper"
    elif ((choice_name=='Rock' and comp_choice_name=='Lizard')or(choice_name=='Lizard'and comp_choice_name=='Rock')):
        print("Rock Wins")
        final_result = "Rock"
    elif ((choice_name=='Lizard' and comp_choice_name=='Spock')or(choice_name=='Spock'and comp_choice_name=='Lizard')):
        print("Lizard Wins")
        final_result="Lizard"
    elif ((choice_name=='Spock' and comp_choice_name=='Scissor')or(choice_name=='Scissor'and comp_choice_name=='Spock')):
        print("Spock Wins")
        final_result="Spock"
    elif ((choice_name=='Scissor' and comp_choice_name=='Lizard')or(choice_name=='Lizard'and comp_choice_name=='Scissor')):
        print("Scissor Wins")
        final_result="Scissor"
    elif ((choice_name=='Lizard' and comp_choice_name=='Paper')or(choice_name=='Paper'and comp_choice_name=='Lizard')):
        print("Lizard Wins")
        final_result="Lizard"
    elif ((choice_name=='Paper' and comp_choice_name=='Spock')or(choice_name=='Spock'and comp_choice_name=='Paper')):
        print("Paper Wins")
        final_result="Paper"
    elif ((choice_name=='Rock' and comp_choice_name=='Scissor')or(choice_name=='Scissor'and comp_choice_name=='Rock')):
        print("Rock Wins")
        final_result="Rock"
    elif ((choice_name=='Spock' and comp_choice_name=='Rock')or(choice_name=='Rock'and comp_choice_name=='Spock')):
        print("Spock Wins")
        final_result="Spock"

    if choice_name == final_result:
        print("Player Winner")
        return True
    else:
        print("Computer Wins")
        return False

# "This is for Testing please comment while loop while running unit test"
while True:
    result = game()
    print(result)
    print("Do you want to play again(Y/N)")
    ans=input()
    if ans == 'n' or ans == 'N':
        break








