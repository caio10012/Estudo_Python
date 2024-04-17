def jogo_novo():
    guesses=[]
    correct_guess = 0
    question_num = 1
    for key in questoes:
        print(key)
        for i in opcoes[0]:
            print(i)
        guess = input("coloque (A,B,C,D):").upper()
        guesses.append(guess)

        correct_guess+=check_resposta(questoes.get(key),guess)
        question_num+=1
    score(correct_guess,guesses)
#-----------------
def check_resposta(resposta,guess):
    if resposta==guess:
        print("correto!")
        return 1
    else:
        print("errado")
        return 0
#-----------------
def score(correct_guesses,guesses):

#-----------------
def joga_denovo():
    pass
#-----------------

#uso de dicionarios, possuem keys(1) e values(2)
questoes = {
    "quem criou o python? ":"A",
    "quem descobriu o Brasil? ":"B",
    "quem vai ganhar o jogo de hoje? ":"C",
    "quem é o maior time do mundo? ":"D"
}
#lista de listas
opcoes = [["A. tadeu","B . caio","C. joao","D. kane"],
          ["A. cristovão","B . Pedro","C. jasas","D. kasfg"],
          ["A. city","B . real","C. bayern","D. esse"],
          ["A. sporting","B . santa","C. nautico","D. sport"]]

jogo_novo()