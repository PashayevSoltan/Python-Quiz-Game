import random
import time     
from os import system 
from model import * 


def voting():
    total_votes = 100 
    for option, vote in anv.items():
        if option in ["A", "B", "C", "D"]:
            voting = random.randint(1,10)
            numbers_of_stars_and_vote_percentage = voting * 10
            while numbers_of_stars_and_vote_percentage:
                print("*", end = "") 
                break 
            print(f"{option}: {numbers_of_stars_and_vote_percentage} %")

            
def removeing_answers(correct):
    lst = ["A", "B", "C", "D"]
    times = 2
    while times > 0:
        rand = random.randint(0, len(lst)-1)
        index = lst.index(correct.upper())
        if rand != index:
            lst.pop(rand)
            times -= 1
    return lst
 
def shuffle_answer(lst):
    list_to_shuffle = lst[0]
    answer = lst[1]
    element = list_to_shuffle[anv.get(answer)-1]

    random.shuffle(list_to_shuffle)
    new_index = list_to_shuffle.index(element)

    return list_to_shuffle, anv.get(new_index+1)

def ask_question(rand):
    global joker_count 
    joker_count = 0 
    global bal 
    joker = 0 
    if not rand in already_used_questions:
        while True: 
            system("cls")
            already_used_questions.append(rand)
            if joker != 1:
                result = shuffle_answer(answers[rand])
            answer, correct = result
            main_list = ["A", "B", "C", "D"]
            print(f'\n{questions[rand]}')
            
            if joker == 1:
                new_answer = removeing_answers(correct) 
                index = 0
                for item in main_list:
                    if item in new_answer:
                        print(f'{item}. {answer[index]}', end=' ')
                    else:
                        print(f'{item}. ---', end=' ')
                    index += 1
                print()
            else:
                print(f"\nA. {answer[0]} B. {answer[1]} C. {answer[2]} D. {answer[3]}")
            
            user_input = input("Answer: ").upper()
            if user_input == correct:
                print("Correct Answer! You Earned 1500 azn!")
                bal += 1500
                time.sleep(2)
                break 
            else:
                print("Incorrect answer!")
                joker_input = input("Do you want to use joker chance? [Y/N]: ")
                if joker_input.upper() == "Y":
                    if joker_count == 1:
                        run = False
                        print("You can't use joker chances 2 times")
                        print("You lose the game Good bye -_- SO BAD HAHAHAHA") 
                        return run 
                    joker_count += 1
                    joker_choice = input("R- Remove 2 incorrect answers, V- voting by viewers: ") 
                    if joker_choice == "R":
                         joker = 1
                         continue
                    elif joker_choice == "V":
                        voting()
                    else:
                        print("You didn't use your joker chance and your answer is incorrect and unfortunately you lose the game -_- Good Bye! HAHHAH") 
                    joker = 1
                    continue
                else:
                    print("You lose the game Good bye -_- SO BAD HAHAHAHA")
                    print(f"You earned only {bal} azn Good Luck! HAHA")
                    run = False 
                    return run 

def main():
    run = True
    while len(already_used_questions) < 5 and run:
        q = random.randint(0, 4)
        run = ask_question(q)
        if run is None:
            run = True
    
main()