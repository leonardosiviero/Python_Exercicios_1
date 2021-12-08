#Faça um programa que leia e valide as seguintes informações:
#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd'; 

lenght = 0
salario = 0
listaSexo = ["F", "f", "M", "m"]
sexo = "j"
listaEstado = ["S", "s", "C", "c", "V", "v", "D", "d"]
estadoCivil = "z"

while lenght < 3:
    nome = input("Insira seu nome: ")
    lenght = len(nome)

while salario <= 0:
     salario = float(input("Digite seu salário: "))

while sexo not in listaSexo:
    sexo = str(input("Digite seu sexo (M/F): "))

while estadoCivil not in listaEstado:
    estadoCivil = str(input("Insira se estado civil (S/C/V/D): "))

print("Nome: ", nome)
print("Salário: R${:.2f}".format(salario))
print("Sexo :", sexo)
print("Estado Civil: ", estadoCivil)