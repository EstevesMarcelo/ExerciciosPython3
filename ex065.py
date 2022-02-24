# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

i = 0
n = 0
s = 0
m = True
z = ''
maior = 0
menor = 0
while True:
    s = int(input('Digite um número: '))
    i += 1
    n += s
    if i == 1:
        maior = s
        menor = s
    else:
        if s > maior:
            maior = s
        elif s < menor:
            menor = s
    z = str(input('Deseja continuar [S/N]?').upper()).strip()[0]
    if z == 'N':
        print("Encerrado")
        break
    while z != 'N' and z != 'S':
        print('Comando inválido. Tente outra vez.')
        z = str(input('Deseja continuar [S/N]?').upper()).strip()[0]

print('A média entre os valores foi {:.2f}.'.format(n/i))
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi', menor)
