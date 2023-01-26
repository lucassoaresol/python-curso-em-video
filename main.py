distancia = float(input('Uma distância em metros: '))
print(f'A media de {distancia}m corresponde a')
print(f"""{distancia/1000}km
{distancia/100}hm
{distancia/10}dam
{distancia*10:.0f}dm
{distancia*100:.0f}cm
{distancia*1000:.0f}mm""")
