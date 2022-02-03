# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

'''import random
sorteio = []
print('-=-'*30)
print('Auxiliador de apostas')
print('-=-'*30)
print()
aux = []
b = []
for t in range(1, 61):
    aux.append(t)

a = int(input('Quantos jogos deseja fazer? '))
if a == 1:
    b = random.sample(aux, 6)
    b.sort()
    sorteio.append(b[:])
    print('A sua sugestão de jogo é:\n{}'.format(sorteio))
elif a > 1:
    for i in (1, a+1):
        b = random.sample(aux, 6)
        b.sort()
        sorteio.append(b[:])
    print(f'As suas sugestões para apostas são: \n{sorteio}')'''


# Solução Guanabara

from random import randint
from time import sleep

lista = list()
jogos = list()
print('-'*30)
print('          JOGA NA MEGA SENA          ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '<BOA SORTE>', '-='*5)
