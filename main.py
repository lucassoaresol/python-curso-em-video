from datetime import datetime

expressao = " bom dia"
hora = int(datetime.now().strftime("%H"))
if hora >= 12 and hora < 18:
    expressao = "a boa tarde"
elif hora >= 18:
    expressao = "a boa noite"
velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print(
        f"""MULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${(velocidade-80)*7:.2f}!"""
    )
print(f"Tenha um{expressao}! Dirija com segurança!")
