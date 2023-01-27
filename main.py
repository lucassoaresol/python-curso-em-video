numero = int(input('Informe um número: '))
print(f"""Analisando o número {numero}
Unidade: {numero // 1 % 10}
Dezena: {numero // 10 % 10}
Centena: {numero // 100 % 10}
Milhar: {numero // 1000 % 10}""")
