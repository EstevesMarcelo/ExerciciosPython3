# Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
'''inverso = [::-1]
Essa técnica de fatiamento elimina a dependência de utilização do for'''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
