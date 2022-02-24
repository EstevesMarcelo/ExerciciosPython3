# Desenvolva um progrema que leia o nome, idade de sexo de 4 pessoas. No final do programa,
# mostre : a média de idade do grupo, qual o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.

from time import sleep
print('\033[36mAnalisador completo\033[m')
print()
print('Iniciando...')
sleep(1)
print()
print('-=-'*20)
print()
s = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Digite seu nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    s += idade
    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
print()
print('A média de idade entre das pessoas é de {}'.format(s/4))
print('O homem mais velho é {} e sua idade é {} anos.'.format(nomevelho, maioridadehomem))
print("A quantidade de mulheres com menos de 20 anos é de {}".format(totmulher20))
print()
print('-=-'*20)
sleep(1)
print()
print('\033[36mFinalizando analisador...\033[m')
