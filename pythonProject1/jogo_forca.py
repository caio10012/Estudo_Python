import random

# escolhendo a palavra


def escolha_palavra():
    palavras = ["caio", "joao", "forever"]
    return random.choice(palavras)

# exibindo a palavra


def exibe_palavra(palavra,letra_correta):
    exibicao = ""
    for letra in palavra:
        if letra in letra_correta:
            exibicao += letra + " "
        else:
            exibicao += "_ "

    return exibicao.strip()

def jogo_forca():
    palavra = escolha_palavra()
    tentativas = 8
    letra_correta = []
    letra_errada = []

    print("Bem vindo ao jogo da forca!")

    while tentativas > 0:
        print("\n" + exibe_palavra(palavra,letra_correta))
        print(f"voce tem {tentativas} restantes.")
        print(f"voce ja tentou essas letras:" +"".join(letra_errada))
        tentativa = input("tente adivinha a letra:")
        if tentativa in letra_correta or tentativa in letra_errada:
            print("essa letra ja foi usada!")
        elif tentativa in palavra:
            letra_correta.append(tentativa)
            if set(letra_correta) == set(palavra):
                print("você ganhou! a palavra era " + exibe_palavra(palavra,letra_correta))
                break
        else:
            letra_errada.append(tentativa)
            print("você errou! a palavra era " + palavra)
            tentativas -= 1


jogo_forca()
