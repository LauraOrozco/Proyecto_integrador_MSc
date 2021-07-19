# pip install pdftotext
# sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev

import pdftotext
import os

path = "."

cont = 0
for root, _, file_names in os.walk(path):
    for file_name in file_names:
        path_file = "%s/%s" % (root, file_name)
        with open(path_file, "rb") as f:
            if file_name.endswith(".pdf"):
                cont = cont + 1
                pdf = pdftotext.PDF(f)
                new_file = open(file_name[:-4] + ".txt", "w+")
                new_file.write("\n\n".join(pdf))
                new_file.close()
print(cont)