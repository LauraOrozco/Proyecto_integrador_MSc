# pip install pdftotext
# sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev

from pdf2image import convert_from_path
from PIL import Image
import pytesseract

import os


def create_images():
    path = "."

    cont = 0
    for root, _, file_names in os.walk(path):
        for file_name in file_names:
            path_file = "%s/%s" % (root, file_name)
            if path_file.endswith(".pdf"):
                images = convert_from_path(path_file)
                images[0].save("images/"+file_name[:-4]+".png")
    print(cont)


def images_to_text():
    for _, _, file_names in os.walk("images"):
        for file_name in file_names:
            text = pytesseract.image_to_string(
                Image.open('images/'+file_name), lang='spa')
            new_file = open("texts/"+file_name[:-4] + ".txt", "w+")
            new_file.write(text)
            new_file.close()


images_to_text()
