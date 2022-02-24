# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. NO final, mostre:
# a) quantas pessoas tem mais de 18 anos;
# b) quantos homens foram cadastrados;
# c) quantas mulheres tem menos de 20 anos.

print('-'*30)
a = 'CADASTRO DE PESSOA'
print(f'{a:^30}')
print('-'*30)
i, h, m = 0, 0, 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        print('Sexo inválido. Digite novamente.')
        sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    print()
    if idade > 18:
        i += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    z = str(input('Deseja cadastrar mais alguém [S/N]? ')).upper().strip()[0]
    print()
    while z != 'S' and z != 'N':
        print('Comando inválido. Tente novamente.')
        z = str(input('Deseja cadastrar mais alguém [S/N]? ')).upper().strip()[0]
        print()
    if z == 'N':
        print('Cadastramento encerrado.')
        break
print()
if i == 0:
    print('Todas as pessoas cadastradas tem menos de 18 anos.')
elif i == 1:
    print('Apenas uma pessoa cadastrada tem mais de 18 anos.')
else:
    print(f'Foram cadastradas {i} pessoas com mais de 18 anos.')
if h == 0:
    print('Nenhum homem foi cadastrado.')
elif h == 1:
    print('Apenas um homem foi cadastrado.')
else:
    print(f'Foram cadastrados {h} homens.')
if m == 0:
    print('Nenhuma mulher cadastrada tem menos de 20 anos.')
elif m == 1:
    print('Apenas uma mulher cadastrada possui menos de 20 anos.')
else:
    print(f'Foram cadastradas {m} mulheres com menos de 20 anos.')
