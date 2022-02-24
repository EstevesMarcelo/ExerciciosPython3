# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre:
# a) qual é o total gasto na compra;
# b) quantos produtos custam mais de R$1000,00;
# c) qual é o nome do produto mais barato.

print('-'*30)
a = 'LOJA SUPER BARATÃO'
print(f'{a:^30}')
print('-'*30)
print()
i, u, v = 0, 0, 0
barato = ''
comp = 0
while True:
    nome = str(input('Produto: ')).title().strip()
    preco = float(input('Preço [R$]: '))
    i += preco
    v += 1
    if v == 1:
        barato = nome
        comp = preco
    if v >= 2:
        if preco < comp:
            comp = preco
            barato = nome
    if preco > 1000:
        u += 1
    print()
    z = str(input('Deseja cadastrar mais algum produto? [S/N] ')).upper().strip()[0]
    while z != 'S' and z != 'N':
        print('Comando inválido. Tente novamente.')
        z = str(input('Deseja cadastrar mais algum produto? [S/N] ')).upper().strip()[0]
        print()
    if z == 'N':
        print('Coleta de dados encerrada.')
        break
print()
print(f'O total gasto na compra foi de R${i}.')
if u == 0:
    print('Nenhum item na sua lista de compras custou mais de R$1000,00.')
elif u == 1:
    print('Apenas 1 item comprado custou mais de R$1000,00.')
else:
    print(f"De todos os produtos comprados, {u} custam mais de R$1000,00.")
print(f'O nome do item mais barato é {barato}.')
