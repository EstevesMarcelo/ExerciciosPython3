# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade
# c) Uma lista com as mulheres
# d) Uma lista de pessoas com idade acima da média

dados, mul, ida = [], [], []
inf = {}
u = 0
while True:
    inf['Nome'] = str(input('Informe o nome: ')).title().strip()
    inf['Sexo'] = str(input('Informe o sexo [M/F]: ')).title().strip()[0]
    if inf['Sexo'] != 'M' and inf['Sexo'] != 'F':
        print('Informação inválida. Digite novamente!')
    inf['Idade'] = int(input('Informe a idade: '))
    dados.append(inf.copy())
    inf.clear()
    a = str(input('Quer continuar? [S/N]')).title().strip()[0]
    if a != 'S' and a != 'N':
        print('Comanda inválido. Digite novamente.')
    elif a == 'N':
        break
print()
print('-=-'*30)
print(f'{"Resultado":^80}')
print('-=-'*30)
if len(dados) == 1:
    print('Foi cadastrado apenas uma pessoa.')
elif len(dados) > 1:
    print(f'Foram cadastradas {len(dados)} pessoas.')
for i in range(0, len(dados)):
    u = u + dados[i]["Idade"]
    if dados[i]["Sexo"] == 'F':
        mul.append(dados[i]["Nome"][:])
z = u/len(dados)
print(f'A média de idade é de {z} anos.')
if len(mul) == 0:
    print('Não houve cadastro de mulheres.')
elif len(mul) >= 1:
    print('As mulheres cadastradas são:')
    for t in mul:
        print(t)
for g in range(0, len(dados)):
    if dados[g]["Idade"] > z:
        ida.append(dados[g]["Nome"][:])
if len(ida) == 0:
    print('Nenhuma pessoa cadastrada está acima da média.')
elif len(ida) >= 1:
    print('As pessoas cadastradas com idade acima da média são:')
    for m in ida:
        print(m)
