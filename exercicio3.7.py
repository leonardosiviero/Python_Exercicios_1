#Faça um programa que leia 5 números e informe o maior número.

def comparaNumeros():

    lista = []
    count = 0
    maiorNumero = -9999999999

    while count < 5:
        numero = float(input("Digite um número."))
        lista.append(numero)
        count += 1

        if maiorNumero < numero:
            maiorNumero = numero

    print("O maior dos cinco números digitados foi {}".format(maiorNumero))

if (__name__ == "__main__"):
    comparaNumeros()