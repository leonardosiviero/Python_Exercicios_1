#Faça um programa que leia 5 números e informe a soma e a média dos números.

def comparaNumerosSomaMedia():

    lista = []
    count = 0
    maiorNumero = -9999999999
    soma = 0

    while count < 5:
        numero = float(input("Digite um número."))
        lista.append(numero)
        count += 1
        soma = soma + numero

    media = soma / count

    print("A soma dos números é: {}.".format(soma))
    print("A média dos números é: {}.".format(media))

if (__name__ == "__main__"):
    comparaNumerosSomaMedia()