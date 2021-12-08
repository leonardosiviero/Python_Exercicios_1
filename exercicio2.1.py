#Pedir dois numeros e verificar qual e o maior

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

if num1 > num2:
    print("O maior número é o número {}.".format(num1))
else:
    print("O maior número é o número {}.".format(num2))
