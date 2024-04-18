
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("coloque (a,b,c,d)").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(i),guess)
        question_num +=1
    display_score()
def check_answer(correct_guesses,guesses):
    if correct_guesses == guesses:
        return 1
    else:
        return 0

def display_score():
    print("-------------")
    print("RESULTADOS")
    print("-------------")

    print("Respostas", end ="")
    for i in questions:
        print(questions.get(i), end ="")
    print()

    print("guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int(input(correct_guesses/len(questions)) *100)
    print("o seu score é:" +str(score)+"%")

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()


























