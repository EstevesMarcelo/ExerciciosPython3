# Faça um programa que leia um número qualquer e faça seu fatorial.

# Solução 1

'''from math import factorial
n = int(input("Digite um número inteiro para ser calculado: "))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

# Solução 2

n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end="")
while c > 0:
    print('{}'.format(c), end="")
    print(' X ' if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print('{}'.format(f))
