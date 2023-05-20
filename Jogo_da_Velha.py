class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
        }

#formato do tabuleiro em dicionário

    def mostrar_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("└───┴───┴───┘")

#mostrar o placar do jogo

jogo=JogoDaVelha()
jogadorAtual="X"

print(f'''
░░░░░██╗░█████╗░░██████╗░░█████╗░░░░░░░░░██████╗░░█████╗░░░░░░░░░██╗░░░██╗███████╗██╗░░░░░██╗░░██╗░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗░░░░░░░░██╔══██╗██╔══██╗░░░░░░░░██║░░░██║██╔════╝██║░░░░░██║░░██║██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║░░░░░░░░██║░░██║███████║░░░░░░░░╚██╗░██╔╝█████╗░░██║░░░░░███████║███████║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║░░░░░░░░██║░░██║██╔══██║░░░░░░░░░╚████╔╝░██╔══╝░░██║░░░░░██╔══██║██╔══██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝░░░░░░░░██████╔╝██║░░██║░░░░░░░░░░╚██╔╝░░███████╗███████╗██║░░██║██║░░██║
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░░░░░░░░░╚═════╝░╚═╝░░╚═╝░░░░░░░░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝''')

#Processo pra verificação da resposta
while True:

    jogadorAtual=str(input("Qual jogador vai começar?('X' ou 'O')\n")).upper()

    if jogadorAtual != "X" and jogadorAtual != "O":
        print("Valor inválido, digite 'X' ou 'O' ")

    else:
        print(f"Jogador Selecionado: {jogadorAtual}")
        placar = JogoDaVelha()
        placar.mostrar_tabuleiro()
        break

#Primeira jogada

jogada=int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

while jogada < 1 or jogada > 9 or placar.tabuleiro[str(jogada)] != ' ':
    if jogada < 1 or jogada > 9:
        print("Escolha Inválida")
        jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

    else:
        print("Slot Já Prenchido")
        jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

jogo.tabuleiro[str(jogada)] = jogadorAtual
jogo.mostrar_tabuleiro()

if jogadorAtual == "X":
    jogadorAtual = "O"
else:
    jogadorAtual = "X"

#Proximas jogadas
turno=2

for turnos in range (1,9):
    jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

    while jogada < 1 or jogada > 9 or placar.tabuleiro[str(jogada)] != ' ':
        if jogada < 1 or jogada > 9:
            print("Escolha Inválida")
            jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

        else:
            print("Slot Já Prenchido")
            jogada = int(input(f"O jogador '{jogadorAtual}' Vai jogar em qual slot?\nExemplo de slot:(de 1 a 9): "))

    jogo.tabuleiro[str(jogada)] = jogadorAtual
    jogo.mostrar_tabuleiro()

#Condições de vitória Vertical
    if (jogo.tabuleiro['1'] == jogo.tabuleiro['4'] == jogo.tabuleiro['7'] == jogadorAtual or
        jogo.tabuleiro['2'] == jogo.tabuleiro['5'] == jogo.tabuleiro['8'] == jogadorAtual or
        jogo.tabuleiro['3'] == jogo.tabuleiro['6'] == jogo.tabuleiro['9'] == jogadorAtual):

        print(f"{jogadorAtual} VENCEU!!")
        break

#Condições de vitória Horizontal
    if (jogo.tabuleiro['1'] == jogo.tabuleiro['2'] == jogo.tabuleiro['3'] == jogadorAtual or
        jogo.tabuleiro['4'] == jogo.tabuleiro['5'] == jogo.tabuleiro['6'] == jogadorAtual or
        jogo.tabuleiro['7'] == jogo.tabuleiro['8'] == jogo.tabuleiro['9'] == jogadorAtual):

        print(f"{jogadorAtual} VENCEU!!")
        break

#Condições de vitoria Cruzado
    if (jogo.tabuleiro['1'] == jogo.tabuleiro['5'] == jogo.tabuleiro['9'] == jogadorAtual or
        jogo.tabuleiro['3'] == jogo.tabuleiro['5'] == jogo.tabuleiro['7'] == jogadorAtual):

        print(f"{jogadorAtual} VENCEU!!")
        break

     # Verificador de Velha
    if round == 8:
            if not ((jogo.tabuleiro['1'] == jogo.tabuleiro['4'] == jogo.tabuleiro['7'] == jogadorAtual or
                     jogo.tabuleiro['2'] == jogo.tabuleiro['5'] == jogo.tabuleiro['8'] == jogadorAtual or
                     jogo.tabuleiro['3'] == jogo.tabuleiro['6'] == jogo.tabuleiro['9'] == jogadorAtual) or
                    (jogo.tabuleiro['1'] == jogo.tabuleiro['2'] == jogo.tabuleiro['3'] == jogadorAtual or
                     jogo.tabuleiro['4'] == jogo.tabuleiro['5'] == jogo.tabuleiro['6'] == jogadorAtual or
                     jogo.tabuleiro['7'] == jogo.tabuleiro['8'] == jogo.tabuleiro['9'] == jogadorAtual) or
                    (jogo.tabuleiro['1'] == jogo.tabuleiro['5'] == jogo.tabuleiro['9'] == jogadorAtual or
                     jogo.tabuleiro['3'] == jogo.tabuleiro['5'] == jogo.tabuleiro['7'] == jogadorAtual)):
                print("DEU VELHA")

#Troca de Jogador
    turno=turno+1
    print(turno)
    if jogadorAtual== "X":
        jogadorAtual="O"
    else:
        jogadorAtual="X"
    print(f"Agora é a vez do jogador '{jogadorAtual}'")





