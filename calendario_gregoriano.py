ano = int(input("Insira um ano da historia com quatro digitos: "))

if ano < 1582:
    print("Not within the Gregorian calendar period")
elif ano%4 == 0 or ano%400 == 0:
    print("Bissexto")
else:
    print('Ano comum')