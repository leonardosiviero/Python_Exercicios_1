#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

dia = int(input("Insira um numero de 1 a 7 para receber seu respectivo dia da semana: "))

if dia == 1:
    print("Domingo.")
elif dia == 2:
    print("Segunda.")
elif dia == 3:
    print("Terça.")
elif dia == 4:
    print("Quarta.")
elif dia == 5:
    print("Quinta.")
elif dia == 6:
    print("Sexta.")
elif dia == 7:
    print("Sábado.")
else:
    print("Numero fora da série 1 a 7.")