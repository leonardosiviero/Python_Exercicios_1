#Encontrar o maior e o menor de 3 numeros

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

if num1 != maior and num1 != menor:
    numMedio = num1
elif num2 != maior and num2 != menor:
    numMedio = num2
else:
    numMedio = num3

print(maior, numMedio , menor)