#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
a = ('Mexico', 'Marte', 'Rosa', 'Avestruz')
for i in a:
    print(f'\nA palavra {i.upper()} possui as vogais ', end='')
    for letra in i:
        if letra in 'aeiou':
            print (letra, end=' ')
       