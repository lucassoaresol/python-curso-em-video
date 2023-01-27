nome = str(input('Digite seu nome completo: ')).strip()
separa_nome = nome.split()
primeiro_nome = separa_nome[0]
letras = ''.join(separa_nome)
print(f"""Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(letras)} letras
Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras""")
