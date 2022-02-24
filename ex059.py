# crie um programa que leia dois valores e mostre um menu na tela:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# O programa deverá realizar a operação solicitada em cada caso

from time import sleep
print('\033[36mOperador Mutante. Iniciando...\033[m')
print()
print('-=-'*20)
print()
n = 0
a = float(input("Digite o primeiro valor: "))
b = float(input('Digite o segundo valor: '))
while n != 5:
    print()
    print(' [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA')
    print()
    n = int(input('O que deseja fazer? '))
    if n != 1 and n != 2 and n != 3 and n != 4 and n != 5:
        print('Comando inválido. Tente outra vez.')
    if n == 1:
        print("O valor da soma de {} e {} é {}.".format(a, b, a+b))
    if n == 2:
        print('O valor do produto entre {} e {} é {}.'.format(a, b, a*b))
    if n == 3:
        if a > b:
            print("O maior valor informado é {}.".format(a))
        elif a < b:
            print('O maior valor informado é {}.'.format(b))
        else:
            print('Os valores informados são iguais.')
    if n == 4:
        d = float(input('Digite um novo valor: '))
        e = float(input('Digite outro novo valor: '))
        a = d
        b = e
print()
print('\033[36mOperador Mutante concluído com êxito.\033[m')
print()
print('-=-'*20)
print()
print("Finalizando...")
sleep(2)
