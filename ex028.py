# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

import random
print("O seu jogo começará agora!")
print("-=-"*20)
print("Tente adivinhar o número que eu pensei entre 0 e 5")
n = [0,1,2,3,4,5]
n2 = random.choice(n)
m = int(input("Qual número entre 0 e 5 você acha que o computador escolheu?"))
if m == n2:
    print('Você acertou. Parabéns!')
else:
    print('Você errou. O computador venceu.')
