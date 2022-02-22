# Crie um programa que leia dois números e mostre a soma entre eles.

valor1 = input("Digite o primeiro valor")
valor2 = input("digite o segundo valor")
s = int(valor1) + int(valor2)
mensagem = "A soma entre {} e {} é {}"

print(mensagem.format(valor1, valor2, s))

#print("A soma entre", valor1, "e", valor2, "é", int(valor1) + int(valor2))



