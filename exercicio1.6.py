#Cálculo da área de um círculo a partir da dimensão do raio

import math

print("Cálculo de área de uma circunferência.\n")
radius = float(input("Insira a dimiensão do raio: "))
area = math.pi * radius ** 2

print("\n A área da circunferência é: {:.2f}\n".format(area))