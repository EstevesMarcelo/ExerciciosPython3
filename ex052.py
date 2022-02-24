# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Solução particular

'''a = int(input("Digite um número: "))
for i in range(2, a):
    if a % i != 0 :
        print("O número {} é primo .".format(a))
        break
    else:
        print("o número {} não é primo.".format(a))
        break'''

# Solução do Guanabara

num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[36m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\033[mO número {} foi divisível {} vezes.".format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print("E por isso ele NÃO É PRIMO!")
