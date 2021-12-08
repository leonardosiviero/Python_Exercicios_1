#Encontrar o maior de 3 numeros

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é o {}".format(num1))
elif num2 > num1 and num2 > num3:
    print("O maior número é o {}".format(num2))
else:
    print("O maior número é o {}".format(num3))    