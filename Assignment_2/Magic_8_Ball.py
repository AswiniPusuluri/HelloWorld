# Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.
#
# Allow the user to input their question.
# Show an in progress message.
# Create 10/20 responses, and show a random response.
# Allow the user to ask another question/advice or quit the game.

import random

Answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


def MagicBall():
    input('Ask your question:')
    print(Answers[random.randint(0, len(Answers) - 1)])
    Replay()


def Replay():
    print('Do you have another question? [Y/N] ')
    ans = input()
    if ans == 'Y'or ans == 'y':
        MagicBall()
    elif ans == 'N'or ans == 'n':
        exit()
    else:
        print('I apologise.Please repeat.')
        Replay()


MagicBall()
