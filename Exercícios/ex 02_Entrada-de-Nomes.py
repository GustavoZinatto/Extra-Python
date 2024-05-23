# Crie um programa em Python que solicite ao usuário seu nome e a sua idade (em formato de inteiro). 
# O programa deve verificar se a pessoa é maior de idade (18 anos ou mais). 
# Se for maior de idade, deve exibir uma mensagem dizendo que a pessoa é maior de idade; 
# caso contrário, deve informar que a pessoa é menor de idade.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")
    