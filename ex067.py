# Faça um programa que mostre a tabuada de vários números , um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.

print('-'*30)
t = 'TABUADA'
print(f'\033[1;36m{t:^30}\033[m')
print('-'*30)
print()
while True:
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    print()
    print(f'\033[36mA tabuada de {n} é :\033[m ')
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print()
print()
print('A tabuada foi finalizada.')
