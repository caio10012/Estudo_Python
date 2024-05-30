
tabuleiro = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
jogador = "X"
ganhador = None
jogo_acontecendo = True


# fazer o tabuleiro
def imprime_tabuleiro():
    print(tabuleiro[0] + "  |  " + tabuleiro[1] + "  |  " + tabuleiro[2])
    print(tabuleiro[3] + "  |  " + tabuleiro[4] + "  |  " + tabuleiro[5])
    print(tabuleiro[6] + "  |  " + tabuleiro[7] + "  |  " + tabuleiro[8])


# fazer a jogada
def fazer_movimento():
    movimento = int(input("digite o seu movimento: (1-9)"))
    if 0 < movimento < 10 and tabuleiro[movimento - 1] == "-":
        tabuleiro[movimento-1] = jogador
    else:
        print("movimento não permitido")
# check vitoria
def check_horizontal():
    global ganhador
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] and tabuleiro[1] != "-":
        ganhador = tabuleiro[1]
        return True
    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] and tabuleiro[3] != "-":
        ganhador = tabuleiro[4]
        return True
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] and tabuleiro[8] != "-":
        ganhador = tabuleiro[6]
        return True
def check_vertical():
    global ganhador
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] and tabuleiro[1] != "-":
        ganhador = tabuleiro[1]
        return True
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] and tabuleiro[3] != "-":
        ganhador = tabuleiro[0]
        return True
    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] and tabuleiro[2] != "-":
        ganhador = tabuleiro[2]
        return True
def check_diagonal():
    global ganhador
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != "-":
        ganhador = tabuleiro[0]
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[6] != "-":
        ganhador = tabuleiro[2]
        return True

def check_vitoria():
    global jogo_acontecendo
    if check_horizontal() or check_vertical() or check_diagonal():
        print(f"o ganhador foi {ganhador}")
        jogo_acontecendo = False

# check empate
def empate():
    global jogo_acontecendo
    if "-" not in tabuleiro:
        print("a partida deu empate!")
        jogo_acontecendo = False
# troca jogador
def troca_jogador():
    global jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

# jogo em si
def jogo_velha():
    while jogo_acontecendo:
        imprime_tabuleiro()
        fazer_movimento()
        check_vitoria()
        empate()
        troca_jogador()

jogo_velha()