# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a = 0
d = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            a = a + matriz[l][c]
print('-=-'*30)
print('A matriz resultante foi a seguinte:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(0, 3):
    if c == 0:
        d = matriz[1][c]
    else:
        if matriz[1][c] > d:
            d = matriz[1][c]
print()
print(f'A soma de todos os valores pares digitados é: {a}')
b = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores digitados na terceira coluna é: {b}')
print(f'O maior valor da segunda linha é {d}: ')
