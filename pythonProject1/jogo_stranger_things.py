import random

# proporções mapa do stranger things
altura_mapa = 10
largura_mapa = 10

#posisão portal
posicao_portal = [(1, 1)]

#posição monstro
qtd_monstro = 5
posicao_monstro = [(random.randint(0,largura_mapa),random.randint(0,largura_mapa)) for x in range(qtd_monstro)]

#posição personagem
posicao_x = 5
posicao_y = 5

#condição jogo
jogo_acontecendo = True
jogo_acontecendo_2 = True

# imprimindo o mapa
def imprime_mapa():
    for x in range(altura_mapa):
        for y in range(largura_mapa):
            if x == posicao_x and y == posicao_y:
                print("P",end = " ")
            elif (x,y) in posicao_portal:
                print("O",end = " ")
            elif (x,y) in posicao_monstro:
                print("M",end = " ")
            else:
                print("-",end = " ")
        print()

# movimento personagem
def movimenta_personagem(movimento):
    global posicao_x,posicao_y
    if movimento == "w" and posicao_x > 0:
        posicao_x -=1
    elif movimento == "s" and posicao_x < altura_mapa-1:
        posicao_x += 1
    elif movimento == "a" and posicao_y > 0:
        posicao_y -= 1
    elif movimento == "d" and posicao_y < largura_mapa-1:
        posicao_y += 1

def colisao_monstro():
    global posicao_x,posicao_y,posicao_monstro,jogo_acontecendo
    nova_posicao_x = posicao_x
    nova_posicao_y = posicao_y
    ataque_personagem = 80
    ataque_monstro = random.randint(0,84)
    for(mx,my) in posicao_monstro:
        if mx == nova_posicao_x and my == nova_posicao_y:
            if ataque_personagem > ataque_monstro:
                posicao_monstro.remove((mx,my))
                posicao_x = nova_posicao_x
                posicao_y = nova_posicao_y
                print(f"voce matou o monstro, seu ataque foi de {ataque_personagem} e o do monstro foi de {ataque_monstro}")
            else:
                print(f"voce morreu para o monstro, seu ataque foi de {ataque_personagem} e o do monstro foi de {ataque_monstro}")
                jogo_acontecendo = False
        else:
            posicao_x = nova_posicao_x
            posicao_y = nova_posicao_y


def colisao_portal():
    global posicao_x,posicao_y,posicao_portal,jogo_acontecendo
    nova_posicao_x = posicao_x
    nova_posicao_y = posicao_y
    for(mp,mq) in posicao_portal:
        if mp == nova_posicao_x and mq == nova_posicao_y:
            posicao_portal.remove((mp,mq))
            posicao_x = nova_posicao_x
            posicao_y = nova_posicao_y
            print("voce ganhou!!!")
            print("voce está sendo teleportado para o novo mapaaaaaaaaaaa")
            jogo_acontecendo = False
        else:
            posicao_x = nova_posicao_x
            posicao_y = nova_posicao_y

# movimento monstro
def movimento_monstro():
    global posicao_monstro
    nova_posicao_monstro = []
    movimento = random.choice(["w", "a", "s", "d"])
    for(mx,my) in posicao_monstro:
        if movimento == "w" and mx > 0:
            mx -= 1
        elif movimento == "s" and mx < altura_mapa - 1:
            mx += 1
        elif movimento == "a" and my > 0:
            my -= 1
        elif movimento == "d" and my < largura_mapa - 1:
            my += 1
        nova_posicao_monstro.append((mx,my))
    posicao_monstro = nova_posicao_monstro


#imprimindo o mapa da dificuldade 2
def imprime_mapa_2():
    for x in range(altura_mapa * 2):
        for y in range(largura_mapa * 2):
            if x == posicao_x and y == posicao_y:
                print("P",end = " ")
            elif (x,y) in posicao_portal:
                print("O",end = " ")
            elif (x,y) in posicao_monstro:
                print("M",end = " ")
            else:
                print("-",end = " ")
        print()

#jogo
def jogo():
    while jogo_acontecendo:
        imprime_mapa()
        palavras_permitidas = ["w","a","s","d"]
        acao = input("pra onde você quer se movimentar:").lower()
        if acao in palavras_permitidas:
            movimenta_personagem(acao)
            colisao_monstro()
            colisao_portal()
            movimento_monstro()
        else:
            print("movimento não permitido,tente outro")
    imprime_mapa_2()

jogo()
