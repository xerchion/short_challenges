# Enunciado: Crea un programa que sea capaz de transformar texto natural a
# código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
# la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o
# símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
# https://es.wikipedia.org/wiki/Código_morse.

MORSE_CODE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
    }
MORSE_DECODE = {value: key for key, value in MORSE_CODE.items()}


def is_morse(text: str) -> bool:
    vowels = "aeiou"
    for letter in text.lower():
        if letter in vowels:
            return False
    return True


def encode(text):
    message = ""
    words = text.split()
    for word in words:
        for letter in word.upper():
            message += MORSE_CODE[letter] + " "
        message += " "
    return message.rstrip()


def decode(code):
    message = ""
    words = code.split("  ")
    for word in words:
        for letter in word.split(" "):
            message += MORSE_DECODE[letter]
        message += " "
    return message.lower()


def transform(message):
    result = ""
    if is_morse(message):
        result = decode(message)
    else:
        result = encode(message)
    return result
