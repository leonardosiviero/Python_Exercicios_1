#Verificar o sexo F/M

sexo = input("Digite o sexo (F/M): ")
sexo = sexo.upper() #lower para deixar minúscula

if sexo == "F":
    print("Sexo feminino.")
elif sexo == "M":
    print("Sexo masculino.")
else:
    print("Sexo inválido.")
