# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# aguardar solução do Guanabara sobre bases numéricas

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input("Digite sua opção: "))
if opcao == 1:
    print("O número {} convertido para binário é {} .".format(num, bin(num)[2:]))
elif opcao == 2:
    print("O número {} convertido para octal é {} .".format(num, oct(num)[2:]))
elif opcao == 3:
    print("O número {} convertido para hexadecimal é {} .".format(num, hex(num)[2:]))
else:
    print("opção inválida")
