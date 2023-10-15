# Enunciado: Crea un programa se encargue de transformar un número decimal a
# binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


def int_to_bin(num: int) -> str:
    num_bin = ""
    num = int(num)
    while num != 0:
        num_bin = str(num % 2) + num_bin
        num = int(num / 2)
    return num_bin


print(int_to_bin(55))
