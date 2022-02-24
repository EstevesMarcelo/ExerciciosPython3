#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
#de zero até 20.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('-'*30)
print('\033[36mIniciar contador\033[m')
print('-'*30)
a = (
     'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
d ='S'
while d == 'S':
     b = int(input("Digite um número de 0 a 20."))

     if b < 0 or b > 20:
           print('Número inválido. Digite novamente')
           print()
     else:
          print(f'Você digitou o número {a[b]}.')
          print()
          d = input(str('Deseja digitar outro número? [S/N]')).upper().strip()[0]

