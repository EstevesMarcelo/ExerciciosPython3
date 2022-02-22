# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# solução 1
# valor = input("Digite um número entre 0 e 9999")

# milhar = valor[0]
# centena = valor[1]
# dezena = valor[2]
# unidade = valor[3]
# print("Milhar = {} \nCentena = {} \nDezena {} \nUnidade {}".format(milhar, centena, dezena, unidade))

# Solução 2
num = int(input("Digite um número entre 0 e 9999:"))

a = num//1 % 10
b = num//10 % 10
c = num//100 % 10
d = num//1000 % 10

print("Milhar = {} \nCentena = {} \nDezena {} \nUnidade {}".format(d, c, b, a))
