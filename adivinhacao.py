import random

def jogar():

    numero_secreto = random.randrange(1, 101)  # entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1): #+1 porque o último número é exclusivo
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: \n")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você digitou um número inválido. Digite um valor entre 1 e 100.")
            continue

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)  # isso está dentro do bloco else
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()