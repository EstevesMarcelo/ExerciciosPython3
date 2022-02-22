# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Vamos iniciar a análise...")
print("-=-"*20)
a = float(input("Digite um número"))
b = float(input("Digite outro número"))
c = float(input("Digite mais um número"))
if a > b > c:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(a, c))
if a > c > b:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(a, b))
if b > a > c:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(b, c))
if b > c > a:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(b, a))
if c > a > b:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(c, b))
if c > b > a:
    print("O valor {} é o maior dentre os 3 números e o menor é {}.".format(c, a))
print("-=-"*20)
print("Sua análsie foi concluída!")
