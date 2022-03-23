# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
# se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda2

n = float(input("Digite um número:[R$] "))
print(f'Aumentando {moeda2.moeda(n)} em 10%, temos como resultado {moeda2.aumentar(n, True)}')
print(f'Diminuindo {moeda2.moeda(n)} em 10%, temos como resultado {moeda2.diminuir(n, False)}')
print(f'Dobrando {moeda2.moeda(n)}, temos como resultado {moeda2.dobro(n, False)}')
print(f'Dividindo {moeda2.moeda(n)} pela metade, temos como resultado {moeda2.metade(n, True)}')
