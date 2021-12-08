#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

lado1 = float(input("Insira um lado do triângulo: "))
lado2 = float(input("Insira um lado do triângulo: "))
lado3 = float(input("Insira um lado do triângulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo retângulo.")
    else:
        print("Triângulo escaleno.")
else:
    print("Não é um triângulo.")