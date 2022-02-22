# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase:")).lower()

a = frase.count("a")
b = frase.find("a") + 1
c = frase.rfind("a") + 1
print("O caracter a aparece {} vezes na frase. Sua primeira incidência aparece na posição {}"
      " e sua última incidência é na posição {}".format(a, b, c))
