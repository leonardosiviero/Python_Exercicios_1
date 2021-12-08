#Verificar se uma letra é uma vogal ou consoante

def letras():

    vogais = "AEIOU"
    letra = str.upper(input("Digite uma letra: "))

    if letra in vogais:
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")

if (__name__ == "__main__"):
    letras()