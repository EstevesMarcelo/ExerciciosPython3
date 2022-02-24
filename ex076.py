# Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços na
# sequência. No final, mostre uma listagem de preços organizando os dados em forma tabular.

print('-'*35)
a = '\033[36mListagem de preços\033[m'
print(f'{a:^40}')
print('-'*35)
a = ('Lápis', 1.50, 'Caneta', 2.50, 'Tesoura', 4.0, 'Caderno', 40.0, 'Estojo', 8.90, 'Transferidor', 12.30, 'Régua', 8.90)
for i in range(0,len(a)):
    if i % 2 == 0:
        print(f'{a[i]:.<30}', end='')
    elif i % 2 != 0:
        print (f'R$ {a[i]: >7.2f}')
