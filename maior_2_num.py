num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
num3 = int(input("Digite um numero inteiro: "))
maior_num = num1

if maior_num < num2:
    maior_num = num2
if maior_num < num3:
    maior_num = num3
    
print ("O maior número digitado foi: ", maior_num)