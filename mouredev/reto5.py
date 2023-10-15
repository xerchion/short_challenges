# Enunciado: Crea un programa que se encargue de calcular el aspect ratio de
# una imagen a partir de una url.
# Url de ejemplo:
# https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# Hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.


from urllib.request import urlopen

from PIL import Image


def calculate_aspect_ratio(url):
    with urlopen(url) as response:
        image = Image.open(response)
        width, height = image.size
    return round(width / height, 2)


image_url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
aspect_ratio = calculate_aspect_ratio(image_url)

print("Aspec ratio: ", aspect_ratio)
