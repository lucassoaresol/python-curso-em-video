distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45
print(f"E o preço da sua passagem será de R${valor:.2f}")
