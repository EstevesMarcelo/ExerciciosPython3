# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder. mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

import random
print('-'*30)
a = 'Vamos jogar par ou ímpar'
print(f'\033[36m{a:^30}\033[m')
print('-'*30)
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while True:
    c = random.choice(b)
    t = int(input('Escolha um valor: '))
    n = str(input("Você quer par ou ímpar [P/I]: ")).upper().strip()[0]
    while n != 'P' and n != 'I':
        print('Informação inválida. Por favor, tente novamente.')
        n = str(input("Você quer par ou ímpar [P/I]: ")).upper().strip()[0]
    d = t + c
    if d % 2 == 0 and n == 'P':
        i += 1
        print()
        print(f'Você escolheu {t} e eu escolhi {c}. A soma {d} é par.\nVocê venceu.\nVamos jogar novamente.')
        print()
    elif d % 2 == 1 and n == 'I':
        i += 1
        print()
        print(f'Você escolheu {t} e eu escolhi {c}. A soma {d} é ímpar.\nVocê venceu.\nVamos jogar novamente.')
        print()
    elif d % 2 == 0 and n != 'P':
        print()
        print('Você perdeu!')
        print()
        break
    elif d % 2 == 1 and n != 'I':
        print()
        print('Você perdeu!')
        print()
        break
print()
if i == 0:
    print('Você não obteve vitórias nessa partida')
elif i == 1:
    print('Você venceu apenas uma vez nessa partida')
else:
    print(f'GAME OVER! Você obteve nessa partida {i} vitórias consecutivas.')
