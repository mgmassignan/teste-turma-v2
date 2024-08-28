# Programa para imprimir os números ímpares entre 1 e 100
for numero in range(1, 101):  # Itera sobre o intervalo de 1 a 100 (inclusive)
    if numero % 2 != 0:  # Verifica se o número é ímpar
        print(numero, end=" ")  # Exibe o número ímpar sem quebrar a linha