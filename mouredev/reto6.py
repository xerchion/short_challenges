# Enunciado: Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


def turn_around_string(text):
    turned_text = ""
    for letter in text:
        turned_text = letter + turned_text
    return turned_text


print(turn_around_string("Hola mundo"))
