# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a)quantos números foram digitados;
# b) A lista de valores, ordenada em ordem decrescente;
# c) Se o valor 5 foi digitado e está ou não na lista

print('-=-'*30)
print()
lista = []
i = 0
while True:
    a = int(input('Digite um número: '))
    if a in lista:
        print('O número já foi digitado.')
    else:
        print(f'O número digitado foi {a} e ele foi adicionado a lista')
        i = i + 1
        lista.append(a)
    b = input(str('Deseja adicionar outro número?[S/N]')).title().strip()[0]
    if b != 'S' and b != 'N':
        print('Comando inválido. Digite novamente.')
        b = input(str('Deseja adicionar outro número?[S/N]')).title().strip()[0]
    elif b == 'N':
        break
print()
print('-=-'*30)
print()
if i == 1:
    print('Você adicionou apenas um número a lista')
elif i > 1:
    print(f'Você digitou {i} números')
lista.sort(reverse=True)
print(f'A lista de valores, ordenada em ordem decrescente, é: {lista}')
if lista.count(5) == 0:
    print('O número 5 não foi digitado e não está na lista')
elif lista.count(5) == 1:
    print('O número 5 foi digitado e está na lista')
