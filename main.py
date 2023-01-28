cidade = str(input('Em que cidade você nasceu? ')).strip()
cidade_lista = cidade.split()
resposta = cidade_lista[0].upper() == 'SANTO'
print(f'{resposta}')
