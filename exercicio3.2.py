#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

usuario = str(input("Insira um nome de usuario: "))
senha = input("Insira uma senha para o usuario: ")

while usuario == senha:
    print("Usuário e senha não podem ser o mesmo.")
    usuario = str(input("Insira um nome de usuario: "))
    senha = input("Insira uma senha para o usuario: ")

print("Usuario e senha cadastrados.")