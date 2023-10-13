# Reto #1
# ¿ES UN ANAGRAMA?
# Fecha publicación enunciado: 03/01/22
# Fecha publicación resolución: 10/01/22
# Dificultad: MEDIA
#
# Enunciado: Escribe una función que reciba dos palabras (String)
# y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
# otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.


def is_anagrama(word_a, word_b):
    if len(word_a) != len(word_b) or word_a == word_b:
        return False

    for letter in word_a:
        if letter not in word_b:
            return False
        equal_index = word_a.index(letter) == word_b.index(letter)
        if equal_index:
            return False
    return True


print(is_anagrama("Hola", "laoH"))
