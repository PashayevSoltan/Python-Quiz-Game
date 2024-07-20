from model import* 
import random 
import time 
import os 
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
            


def removing_answers(correct): 
    lst = ["A", "B", "C", "D"]
    times = 2
    while times > 0:
        rand = random.randint(0, len(lst)-1)
        index = lst.index(correct.upper())
        if rand != index:
            lst.pop(rand)
            times -= 1
    return lst

result = removing_answers("A")
print(result)

def shuffle_answer(lst):
    list_to_shuffle = lst[0]
    answer = lst[1]
    element = list_to_shuffle[anv[answer]-1]

    random.shuffle(list_to_shuffle)
    new_index = 0 
    for i in range(4):
        if list_to_shuffle[i] == element:
            new_index = i+1
            break

    return list_to_shuffle, anv[new_index]

    
def main():
    global bal 
    global joker_count
    while len(already_used_questions) < 5:
        q = random.randint(0, 4)
        if not q in already_used_questions:
            already_used_questions.append(q)

            result = shuffle_answer(options[q])
            answer, correct = result 
            print(questions[q])
            print(f"\nA. {answer[0]} B. {answer[1]} C. {answer[2]} D. {answer[3]}")
            user_input = input("Answer:").upper()
            if user_input == correct:
                print("Correct answer you earned 1500 azn!")
                bal+=1500
            else:
                joker_input = input("Do you want to use joker? else you will loose the game [Y/N]:")
                if joker_input == "Y":
                    joker_selection = input("Which one do you want to use?For removing 2 incorrect answers- R and for voting- V:")
                    if joker_selection == "R":
                        cor_answers = ["A", "C", "A", "A", "B"]
                        list1 = []
                        for i in cor_answers:
                            list1.append(removing_answers(i))
                            
                    elif joker_selection == "V":
                        voting()
                    else:
                        print("Invalid choice you can choose only R or V") 





