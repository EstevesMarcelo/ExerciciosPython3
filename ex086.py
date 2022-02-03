# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

'''a, b, c = [], [], []
for i in range(1, 4):
    a.append(int(input(f'Digite um valor para a posição [1, {i}]: ')))

for i in range(1, 4):
    b.append(int(input(f'Digite um valor para a posição [2, {i}]: ')))

for i in range(1, 4):
    c.append(int(input(f'Digite um valor para a posição [3, {i}]: ')))

print()
print('A matriz resultante foi:')
print(a)
print(b)
print(c)'''

# Solução guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
