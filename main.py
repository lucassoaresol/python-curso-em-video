nome = str(input('Qual é seu nome completo? ')).upper()
lista_nome = nome.split()
compare = 'SILVA' in lista_nome
print(f'Seu nome tem Silva? {compare}')
