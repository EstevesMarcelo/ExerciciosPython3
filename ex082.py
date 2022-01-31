# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

print('-=-'*30)
print()
lista = []
while True:
    a = int(input('Digite um número: '))
    if a in lista:
        print('O número já foi digitado.')
    else:
        print(f'O número digitado foi {a} e ele foi adicionado a lista')
        lista.append(a)
    b = input(str('Deseja adicionar outro número?[S/N]')).title().strip()[0]
    if b != 'S' and b != 'N':
        print('Comando inválido. Digite novamente.')
        b = input(str('Deseja adicionar outro número?[S/N]')).title().strip()[0]
    elif b == 'N':
        break
lista1 = []
lista2 = []
for i in lista:
    if i % 2 == 1:
        lista1.append(i)
    elif i % 2 == 0:
        lista2.append(i)
lista.sort()
lista1.sort()
lista2.sort()
print()
print(f'A lista com todos os números digitados é a seguinte: {lista}')
if len(lista2) == 0:
    print('Nenhum número par foi digitado e, portanto, não foi produzido uma lista de números pares.')
elif len(lista2) != 0:
    print(f'A lista com os números pares digitados é a seguinte: {lista2}')
if len(lista1) == 0:
    print('Nenhum número ímpar foi digitado e, portanto, não foi produzido uma lista de números ímpares.')
elif len(lista1) != 0:
    print(f'A lista com os números ímpares digitados é a seguinte: {lista1}')
