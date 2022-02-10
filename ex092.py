# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário.Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário.Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Digite o nome: ')).title().strip()
nasc = int(input('Informe o ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('Informe a carteira de trabalho (digite 0 caso não possua): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input('Informe o ano em que foi contratado: '))
    trabalhador['Salário'] = float(input('Informe o salário (em reais): '))
print()
print('-=-'*30)
print()
a = (70 - trabalhador["Idade"])
print(f'O nome do trabalhador é {trabalhador["Nome"]}.')
print(f'{trabalhador["Nome"]} tem {trabalhador["Idade"]} anos.')
if trabalhador['CTPS'] == 0:
    print(f'Ainda não possui carteira de trabalho.')
elif trabalhador['CTPS'] != 0:
    print(f'CTPS associado é {trabalhador["CTPS"]}.')
    print(f'O ano de contratação foi {trabalhador["Ano de contratação"]}.')
    print(f'O salário atual é {trabalhador["Salário"]}.')
    print(f'{trabalhador["Nome"]} precisa de mais {a} anos de contribuição para se aposentar.')
print()
print('-=-'*30)