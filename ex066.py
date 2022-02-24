# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

# Solução 1

i, n, s = 0, 0, 0
while n != 999:
    n = int(input('Digite um número (digite 999 para parar): '))
    if n != 999:
        i += 1
        s += n
    else:
        print("Finalizado")
print(f'Foram digitados {i} números e sua soma é igual a {s}.')

# Solução 2

i, n, s = 0, 0, 0
while True:
    n = int(input('Digite um número (digite 999 para parar): '))
    if n == 999:
        break
    i += 1
    s += n
if i == 0:
    print('Nenhum valor foi passado para a máquina.')
elif i == 1:
    print(f'O único valor digitado foi {s}.')
else:
    print(f'Foram digitados {i} números e sua soma é igual a {s}')
