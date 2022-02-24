# Melhore a questão 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando o usuário disser que quer mostrar 0 termos.

a0 = float(input('Informe o primeiro termo da progressão aritmética: '))
r = float(input('Informe a razão da progressão aritmética: '))
termo = a0
i = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while i <= total:
        print('{} -> '.format(termo), end="")
        termo += r
        i += 1
    print('PAUSA')
    n = int(input('Quantos termos você deseja visualizar a mais? '))
    mais = n
print('A calculadora de progressão aritmética será encerrada com {} termos.'.format(total))
