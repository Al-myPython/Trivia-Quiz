import sys
from termcolor import colored, cprint

def game_instructions():
    # Print instructions to the game
    print('-----------------------------------------------------------------------------------------------------------')
    print("""    Welcome to our first Dynamic Pub Quiz!\n 
    There are 40 questions in all and every correct answer scores 1 point. 
    Questions are either multiple choice or True / False. Your final score will be tallied 
    at the end in the form of percentage correct. The team with the highest percentage wins the game!
    Good luck! / Bonne Chance!\n""")


game_instructions()


def pub_quiz():
    # A multiple choice and True/False Pub Quiz wherein awarded points are commensurate with question difficulty.
    choices = []
    question_num = 1
    blue = 'blue'
    green = 'green'


    for x in questions:
        print()
        print(x)
        for i in options[question_num-1]:
            cprint(i, blue)
        choice = input("Enter (A,B, etc.) here: ",)

        choice = choice.upper()
        choices.append(choice)
        question_num += 1


        if choice == questions.get(x):
            cprint('CORRECT!', green)
        else:
            cprint('Sorry, wrong answer. \nThe correct answer is: ', end='')
            for i in correct_answers[question_num-2]:
                cprint(i, blue, end='')
        if choice != questions.get(x):
            print()

def point_values():
    pass


questions = {
    "1. Lequel des ces expressions en anglais n’est pas lié à la France?": "D",
    "2. Which word below does not fit in this series:": "D",
    "3. Quelle expression ne désigne pas un moment de la journée?": "C",
    "4. Which of the following does NOT designate a mixed alcoholic drink?": "D"}

options = [["A. French fries", "B. French kiss", "C. French leave", "D. Dutch treat"],
           ["A. dog", "B. frog", "C. bog", "D. Fort Huachuca"],
           ["A. Au chant du coq", "B. Dès potron-minet", "C. Du coq à l’ane", "D. Entre chien et loup"],
           ["A. A Bloody Mary", "B. Sex on the Beach", "C. A Harvey Wallbanger", "D. A Screwball"]]

correct_answers = ('D. Dutch treat', 'D. Fort Huachuca', 'C. Du coq à l’ane', 'D. A Screwball',)
points = (1,1,2,2)

pub_quiz()
