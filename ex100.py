# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
numeros = []


def sorteia(lista):
    for i in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Os números sorteados foram: {numeros}')


def somaPar(lista):
    u = 0
    for i in numeros:
        if i % 2 == 0:
            u = u + i
    print(f'O valor da soma de todos os números pares sorteados é {u}.')


sorteia(numeros)
somaPar(numeros)
