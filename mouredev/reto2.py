# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Fecha publicación enunciado: 10/01/22
# Fecha publicación resolución: 17/01/22
# Dificultad: DIFÍCIL
#
# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de
# Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...


# v3
def fibonacci_3():
    numbers = [0, 1]
    while len(numbers) < 50:
        numbers.append(numbers[-1] + numbers[-2])
    print(",".join(map(str, numbers)))


# v2
def fibonacci_2():
    numbers = [0, 1]
    while len(numbers) < 50:
        numbers.append(numbers[-1] + numbers[-2])
    for n in numbers:
        print(n, end="," if numbers.index(n) != numbers.index(numbers[-1]) else "")


# v1
def fibonacci():
    numbers = [0, 1]
    while len(numbers) < 50:
        numbers.append(numbers[-1] + numbers[-2])
    for n in numbers:
        print(n, end=",")
