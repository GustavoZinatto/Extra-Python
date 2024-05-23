# Crie um programa que solicite ao usuário três notas (em formato de ponto flutuante) e calcule a média dessas notas. 
# Em seguida, exiba a média na tela.

# Requisitos:

# O programa deve solicitar ao usuário que insira três notas.
# Ele deve calcular a média dessas notas usando a fórmula: média = (nota1 + nota2 + nota3) / 3.
# Exibir a média na tela.

def calcularMedia(a, b, c):
    return (a + b + c) / 3

a = float (input("Digite a primeira nota: "))
b = float (input("Digite a segunda nota: "))
c = float (input("Digite a terceita nota: "))

media = calcularMedia(a, b, c)

print("A média do Aluno é ", media)