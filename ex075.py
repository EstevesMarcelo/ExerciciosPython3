# Desenvolva um programa que leia quatro valores quatro valores pelo teclado e guarde-os em uma tupla
# No final, mostre:
#  a) Quantas vezes apareceu o número 9
#  b) Em que posição foi digitado o primeiro valor 3
#  c) Quais foram os números pares

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite outro valor: '))
d = int(input('Digite um último valor: '))
e = (a, b, c, d)

# num = (int(input('Digite um valor: ')),
#        int(input('Digite outro valor: ')),
#        int(input('Digite outro valor: ')),
#        int(input('Digite um último valor: ')))

g = ()
print('-'*30)
if e.count(9) == 0:
    print('O número 9 não foi digitado.')
elif e.count(9) ==1:
    print('O número 9 apareceu uma vez.')
else:
    print(f'O número 9 apareceu {e.count(9)} vezes.')
print('-'*30)
if 3 not in e:
    print('O número 3 não foi digitado.')
else:
    print(f'O número 3 teve sua ocorrência na {e.index(3) +1}ª posição.')
print('-'*30)
print(f'Os números pares inseridos foram: ', end='')
for i in e:
    if i % 2 == 0:
        print('->',i, end=' ')
