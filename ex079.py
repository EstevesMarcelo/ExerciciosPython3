# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados
# em ordem crescente.
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
            print('Você escolheu um número duplicado. Não será adicionado!')
    d = input('Deseja adicionar outro número? [S/N]').upper()[0]
    while d != 'N' and d != 'S':
        print('Comando inválido. Tente novamente.')
        d = input('Deseja adicionar outro número? [S/N]').upper()[0]
    if d == 'N':
        break
print()
lista.sort()
print('-=-'*30)
if len(lista) == 1:
    print(f'O número que você escolheu foi:{lista}')
elif len(lista) > 1:
    print(f'Os números que você escolheu foram:{lista}')
