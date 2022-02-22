# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Insira seu nome completo")).strip()
nome1 = nome.upper()
a = 'SILVA' in nome1
print("A incidência de Silva no nome é {}".format(a))
