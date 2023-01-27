from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
angulo_radiano = radians(angulo)
print(f"""O ângulo de {angulo:.1f} tem o SENO de {sin(angulo_radiano):.2f}
O ângulo de {angulo:.1f} tem o COSSENO de {cos(angulo_radiano):.2f}
O ângulo de {angulo:.1f} tem o TANGENTE de {tan(angulo_radiano):.2f}""")
