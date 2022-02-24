# crie na tela um programa que mostre todos os números pares de 1 a 50.

# Solução 1
s = []
for i in range(1, 51):
    if i % 2 == 0:
        s = s + [i]
print(s)
print("Acabou")

# Solução 2

for n in range(2, 51, 2):
    print(n, end=" ")
print("Acabou")
