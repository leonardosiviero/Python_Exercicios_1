#Verificar se uma letra é uma vogal ou consoante

letra = input("Digite uma letra do alfabeto: ")

if letra in "aeiou":
    print("É uma vogal.")
else:
    print("É uma consoante.")