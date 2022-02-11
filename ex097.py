# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    a = len(msg) + 4
    print('-=-'*a)
    print(f'  {msg}')
    print('-=-'*a)


msg = str(input('Insira um nome:'))
escreva(msg)
