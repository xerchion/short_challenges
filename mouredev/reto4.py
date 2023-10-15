# Reto #4
# ÁREA DE UN POLÍGONO
# Fecha publicación enunciado: 24/01/22
# Fecha publicación resolución: 31/01/22
# Dificultad: FÁCIL
#
# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea
# capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

from math import sqrt


def area(side1, side2=0, side3=0):
    # Square or Rectangle
    if side3 == 0:
        side2 = side1 if side2 == 0 else side2
        return side1 * side2
    # Triangle
    else:
        s = (side1 + side2 + side3) / 2
        return sqrt(s * (s - side1) * (s - side2) * (s - side3))


print("Cuadrado: ", area(2))
print("Rectangulo: ", area(2, 3))
print("Triangulo: ", area(5, 7, 8))
