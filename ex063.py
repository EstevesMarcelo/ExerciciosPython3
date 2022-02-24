# Escreve um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma sequência de Fibonacci.

print('\033[36mVamos fazer a sequência de Fibonacci...\033[m')
print()
print('-=-'*20)
print()
n = int(input("Quantos termos você quer mostrar: "))
n1 = 0
n2 = 1
lim = n
i = 3
print('{} -> {} '.format(n1, n2), end='')
'''n1, n2, n1+n2,n1+2n2, 2n1 + 3n2, 3n1 + 5n2, 5n1 + 8n2, '''
while i <= lim:
    n3 = n1 + n2
    print('-> {} '.format(n3), end='')
    n1 = n2
    n2 = n3
    i += 1
print('Fim')
