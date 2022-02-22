# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas e minúsculas.
# b) Quantas letras ao todo sem considerar espaços.
# c) Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo")

nome1 = nome.upper()
nome2 = nome.lower()
a = nome.split()
b = "".join(a)
nome3 = len(b)
nome4 = len(a[0])
print("Analisando seu nome...")
print("Seu nome todo em letras maiúsculas é {}".format(nome1))
print("Seu nome todo em letras minúsculas é{}".format(nome2))
print("O número de letras que seu nome completo possui é {}".format(nome3))
print("Seu primeiro nome possui {} letras".format(nome4))
