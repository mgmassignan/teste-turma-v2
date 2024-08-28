# Programa para ler 10 inteiros e calcular a soma e a média
numeros = []
for i in range(10):  # Solicita 10 números ao usuário
    try:
        numero = int(input("Digite um número inteiro: "))  # Solicita um número inteiro e adiciona à lista
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!")  # Trata entradas que não podem ser convertidas para inteiro

soma = sum(numeros)  # Calcula a soma dos números na lista
media = soma / len(numeros)  # Calcula a média dos números
print("Soma:", soma)  # Exibe a soma
print("Média:", media)  # Exibe a média