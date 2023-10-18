# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
# automáticamente.

def words_counter(text):
    counter = {}
    word = ""
    text = text.lower()
    for letter in text:
        if letter == " ":
            counter[word] = 1 if word not in counter else int(counter[word]) + 1
            word = ""
            continue
        else:
            if letter in ",.":
                continue
            word += letter
    for word in counter.items():
        print(f"La palabra {word[0]} se repite {word[1]} veces")
