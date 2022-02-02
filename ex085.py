# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final,mostre os valores pares e ímpares em ordem crescente.

print()
print('-=-'*30)
print()
lista, par, impar = [], [], []
for i in range(1, 8):
    a = int(input('Digite um número: '))
    if a % 2 == 0:
        par.append(a)
    elif a % 2 == 1:
        impar.append(a)
par.sort()
impar.sort()
print()
print('-=-'*30)
print()
print(f'Os valores pares digitados foram {par}')
print(f'Os valores ímpares digitados foram {impar}')
