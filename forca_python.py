import random

resp="sim"
while resp=="sim" or resp=="s":

    PalavraSelecionada = []
    PalavraDividida = []
    placar = []
    AnimaisSecretas = ["leao", "urso", "rato", "girafa", "tigre", "foca", "baleia", "jacare", "leopardo","axolote"]

    PalavraSelecionada.append(random.choice(AnimaisSecretas))

    for letra in PalavraSelecionada[0]:
        PalavraDividida.append(letra)

    contLetra = 0

    for espaco in PalavraDividida:
        contLetra = contLetra + 1
        placar.append("_")

    print("****" * 20)
    print("                              JOGO DA FORCA")
    print("****" * 20)
    print("")
    print(f"A palavra tem: {contLetra} letras\n{placar}")

    chances=5

    while True:

        if chances==0:
            print("VOCE PERDEU!!")
            break

        print(f"Voce tem {chances} chances")
        chute = input("\nDigite uma letra ou digite 'chutar' para adivinhar a palavra: ").lower()

        if chute == "chutar":
            palavra_chute = input("Digite a palavra completa: ").lower()

            if palavra_chute == PalavraSelecionada[0]:
                print("Parabéns! Você acertou a palavra!")
                break
            else:
                print("Você errou a palavra!")
                chances=chances-1

        elif len(chute) == 1:
            acertou = False

            for i, letra in enumerate(PalavraDividida):
                if chute == letra:
                    placar[i] = letra
                    acertou = True

            if acertou:
                print(f"Letra '{chute}' está na palavra!\n{placar}")
            else:
                print(f"Letra '{chute}' não está na palavra!\n{placar}")
                chances=chances-1

        else:
            print("Entrada inválida! Digite apenas uma letra ou 'chutar' para adivinhar a palavra.")

    resp=str(input("Quer jogar novamente? ")).lower()