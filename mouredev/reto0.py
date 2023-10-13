# Reto #0
# EL FAMOSO "FIZZ BUZZ"
# Fecha publicación enunciado: 27/12/21
# Fecha publicación resolución: 03/01/22
# Dificultad: FÁCIL
# Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100
# (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


# v1.0
def fizz_buzz_numbers():
    for i in range(1, 101):
        result = i
        if i % 3 == 0:
            result = "fizz"
        if i % 5 == 0:
            result = "buzz"
        if i % 3 == 0 and i % 5 == 0:
            result = "fizzbuzz"
        print(result)


# fizz_buzz_numbers()


# v2
def fizz_buzz_numbers_2():
    for i in range(1, 101):
        result = i
        result = "fizz" if i % 3 == 0 else result
        result = "fizz" if i % 3 == 0 else result
        result = "fizzbuzz" if i % 3 == 0 and i % 5 == 0 else result
        print(result)


# fizz_buzz_numbers_2()


# v3
def fizz_buzz_numbers_3():
    def fizz(num):
        if num % 3 == 0:
            return "fizz"
        return ""

    def buzz(num):
        if num % 5 == 0:
            return "buzz"
        return ""

    for i in range(1, 101):
        result = i
        if fizz(i) or buzz(i):
            result = fizz(i) + buzz(i)
        print(result)


# fizz_buzz_numbers_3()


# v3.1
def fizz_buzz_numbers_31():
    def fizz(num):
        return "fizz" if num % 3 == 0 else ""

    def buzz(num):
        return "buzz" if num % 5 == 0 else ""

    for i in range(1, 101):
        result = i
        result = fizz(i) + buzz(i) if fizz(i) or buzz(i) else i
        print(result)


fizz_buzz_numbers_31()


# v3.2
def fizz_buzz_numbers_32():
    def fizz(num):
        return "fizz" if num % 3 == 0 else ""

    def buzz(num):
        return "buzz" if num % 5 == 0 else ""

    for i in range(1, 101):
        print(fizz(i) + buzz(i) if fizz(i) or buzz(i) else i)


# fizz_buzz_numbers_32()


# v4.0
def fizz_buzz_numbers_4():
    def oper(num, target, message):
        return message if num % target == 0 else ""

    for i in range(1, 101):
        fizz = oper(i, 3, "fizz")
        buzz = oper(i, 5, "buzz")
        print(fizz + buzz if fizz or buzz else i)


# fizz_buzz_numbers_4()


# v4.1
def fizz_buzz_numbers_41() -> None:
    def check(num: int, target: int, message: str) -> str:
        return message if num % target == 0 else ""

    for i in range(1, 101):
        fizz = check(i, 3, "fizz")
        buzz = check(i, 5, "buzz")
        print(fizz + buzz if fizz or buzz else i)


fizz_buzz_numbers_41()
