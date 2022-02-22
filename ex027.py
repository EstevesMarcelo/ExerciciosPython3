# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida  primeiro e o último nome
# separadamente.

nome = str(input("Digite seu nome completo")).strip()
nome1 = nome.title()

a = nome1.split()
b = a[0]
c = a[len(a)-1]
print("Muito prazer em te conhecer")
print("Seu primeiro nome é {} e seu último nome é {}".format(b, c))
