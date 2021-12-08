#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
nota = 999
alfa = 2

while nota not in range (0 , 11):
    nota = float(input("Insira uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        break
    print("Valor não está dentro do critério.")

print("O valor da nota é: {}".format(nota))