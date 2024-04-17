import random

while True:
    escolhas = ["pedra", "papel", "tesoura"]
    computador = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input("Pedra, Papel ou Tesoura? ").lower()

    if jogador == computador:
        print("Computador escolheu:", computador)
        print("Jogador escolheu:", jogador)
        print("empatou")
    elif jogador=="pedra":
        if computador =="papel":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("Computador venceu")
        if computador =="tesoura":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("Jogador venceu")
    elif jogador=="papel":
        if computador =="tesoura":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("Jogador venceu venceu")
        if computador =="pedra":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("computador venceu")
    elif jogador=="tesoura":
        if computador =="papel":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("jogador venceu")
        if computador =="pedra":
            print("Computador escolheu:", computador)
            print("Jogador escolheu:", jogador)
            print("computador venceu")
    jogar_denovo = input("jogar de novo:(sim/não):?").lower()

    if jogar_denovo != "sim":
        break
print("tchau")