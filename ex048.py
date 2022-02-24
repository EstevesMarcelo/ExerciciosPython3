# crie um programa que calcule a soma de todos os números ímpares que são múltiplos
# de 3 e que se encontram no intervalo de 1 a 500.

# Solução 1

s = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        s = s + i
print(s)

# Solução 2

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print("A soma dos {} termos solicitados é {}.".format(cont, soma))
