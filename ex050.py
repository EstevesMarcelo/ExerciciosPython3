# Desenvolva um programa que leia s6 números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Solução 1

a = int(input("Digite um número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))
e = int(input("Digite o quinto número: "))
f = int(input("Digite o sexto número: "))
h = [a, b, c, d, e, f]
s = 0
for i in range(0, 6):
    if h[i] % 2 == 0:
        s = s + h[i]
print(s)

# Solução 2

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {} número: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print("Você informou 1 número par e seu valor é {}.".format(soma))
else:
    print("Você informou {} números pares e sua soma é igual a {}.".format(cont, soma))
