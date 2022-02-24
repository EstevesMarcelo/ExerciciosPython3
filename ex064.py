# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles.

n = 0
i = 0
s = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para PARAR]: '))
    if n != 999:
        i +=1
        s += n
    else:
        print()
        print('Finalizado')
        print()
if i == 1:
    print('Você digitou 1 valor, sendo ele {}.'.format(s))
else:
    print('Você digitou {} valores e sua soma é igual a {}.'.format(i, s))
