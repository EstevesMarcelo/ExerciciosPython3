# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e menor valor digitado, além de sua respectiva posição na lista.
valores = []
for i in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
u, w = valores[0], valores[0]
y, z = 0, 0
for pos, k in enumerate(valores):
    if k > u:
        u = k
        y = pos + 1
    elif k <= w:
        w = k
        z = pos + 1
print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {u} que se encontra na {y}ª posição.\n'
      f'O menor número digitado foi {w} que se encontra na {z}ª posição.')

# Solução Guanabara

# listanum = []
# mai = 0
# men = 0
# for c in range(0, 5):
#     listanum.append(int(input(f'Digite um valor para a posição {c}:')))
#     if c == 0:
#         mai = men = listanum[c]
#     else:
#         if listanum[c] > mai:
#             mai = listanum[c]
#         if listanum[c] < men:
#             men = listanum[c]
# print('=-'*30)
# print(f'Você digitou os valores {listanum}')
# print(f'O maior valor digitado foi {mai} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == mai:
#         print(f'{i}...', end='')
# print()
# print(f'O menor valor digitado foi {men} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == men:
#         print(f'{i}...', end='')
# print()
