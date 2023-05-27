class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
        }

    def mostrar_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("└───┴───┴───┘")

resp = "sim"
while resp == "sim":
    jogo = JogoDaVelha()
    jogadorAtual = "X"

    print(f'''
    ░░░░░██╗░█████╗░░██████╗░░█████╗░░░░░░░░░██████╗░░█████╗░░░░░░░░░██╗░░░██╗███████╗██╗░░░░░██╗░░██╗░█████╗░
    ░░░░░██║██╔══██╗██╔════╝░██╔══██╗░░░░░░░░██╔══██╗██╔══██╗░░░░░░░░██║░░░██║██╔════╝██║░░░░░██║░░██║██╔══██╗
    ░░░░░██║██║░░██║██║░░██╗░██║░░██║░░░░░░░░██║░░██║███████║░░░░░░░░╚██╗░██╔╝█████╗░░██║░░░░░███████║███████║
    ██╗░░██║██║░░██║██║░░╚██╗██║░░██║░░░░░░░░██║░░██║██╔══██║░░░░░░░░░╚████╔╝░██╔══╝░░██║░░░░░██╔══██║██╔══██║
    ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝░░░░░░░░██████╔╝██║░░██║░░░░░░░░░░╚██╔╝░░███████╗███████╗██║░░██║██║░░██║
    ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░░░░░░░░░╚═════╝░╚═╝░░╚═╝░░░░░░░░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝''')

    while True:
        jogadorAtual = str(input("Qual jogador vai começar?('X' ou 'O')\n")).upper()

        if jogadorAtual != "X" and jogadorAtual != "O":
            print("Valor inválido, digite 'X' ou 'O' ")
        else:
            print(f"Jogador Selecionado: {jogadorAtual}")
            placar = JogoDaVelha()
            placar.mostrar_tabuleiro()
            break

    jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

    while jogada < 1 or jogada > 9 or placar.tabuleiro[str(jogada)] != ' ':
        if jogada < 1 or jogada > 9:
            print("Escolha Inválida")
            jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))
        else:
            print("Slot Já Preenchido")
            jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

    jogo.tabuleiro[str(jogada)] = jogadorAtual
    jogo.mostrar_tabuleiro()

    if jogadorAtual == "X":
        jogadorAtual = "O"
    else:
        jogadorAtual = "X"

    vencedor = False
    turno = 2

    for turnos in range(1, 9):
        jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

        while jogada < 1 or jogada > 9 or placar.tabuleiro[str(jogada)] != ' ':
            if jogada < 1 or jogada > 9:
                print("Escolha Inválida")
                jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))
            else:
                print("Slot Já Preenchido")
                jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

        jogo.tabuleiro[str(jogada)] = jogadorAtual
        jogo.mostrar_tabuleiro()

        if (placar.tabuleiro['1'] == placar.tabuleiro['4'] == placar.tabuleiro['7'] == jogadorAtual or
            placar.tabuleiro['2'] == placar.tabuleiro['5'] == placar.tabuleiro['8'] == jogadorAtual or
            placar.tabuleiro['3'] == placar.tabuleiro['6'] == placar.tabuleiro['9'] == jogadorAtual or
            placar.tabuleiro['1'] == placar.tabuleiro['2'] == placar.tabuleiro['3'] == jogadorAtual or
            placar.tabuleiro['4'] == placar.tabuleiro['5'] == placar.tabuleiro['6'] == jogadorAtual or
            placar.tabuleiro['7'] == placar.tabuleiro['8'] == placar.tabuleiro['9'] == jogadorAtual or
            placar.tabuleiro['1'] == placar.tabuleiro['5'] == placar.tabuleiro['9'] == jogadorAtual or
            placar.tabuleiro['3'] == placar.tabuleiro['5'] == placar.tabuleiro['7'] == jogadorAtual):

            print(f"{jogadorAtual} VENCEU!!")
            vencedor = True
            break

        turno += 1
        if jogadorAtual == "X":
            jogadorAtual = "O"
        else:
            jogadorAtual = "X"

    if turno == 9 and not vencedor:
        print("DEU VELHA")

    resp = input("Deseja jogar novamente? (Digite 'sim' para jogar novamente): ").lower()
    if resp != "sim":
        break



