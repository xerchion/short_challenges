# ¿ES UN NÚMERO PRIMO?
# Fecha publicación enunciado: 17/01/22
# Fecha publicación resolución: 24/01/22
# Dificultad: MEDIA
#
# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

from math import sqrt


def is_prime_number(number: int) -> bool:
    if number == 0:
        return False
    if int(number / 2) > 1 and number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)), 2):
        if number % i == 0:
            return False
    return True


i = 0
while i < 100:
    if is_prime_number(i):
        print(i)
    i += 1
