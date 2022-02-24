# Melhore o jogo do desafio 28.
# O computador vai ''pensar '' em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
print("\033[36mO seu jogo começará agora!\033[m")
print()
print("-=-"*20)
print()
print("Tente adivinhar o número que eu pensei entre 0 e 10")
print()
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n2 = random.choice(n)
s = 0
m = 0
while m != n2:
    n2 = random.choice(n)
    m = int(input("Qual número entre 0 e 10 você acha que o computador escolheu?"))
    print()
    s += 1
    if m != n2:
        print('Você errou. O computador havia escolhido {} . Tente outra vez\n '.format(n2))
    else:
        if s == 1:
            print('Você acertou. Parabéns! Foi necessária uma tentativa apenas\n ')
        else:
            print("Você acertou. Parabéns! Foram necessárias {} tentativas.\n ".format(s))
print()
print('\033[36mFim do jogo.\033[m')
