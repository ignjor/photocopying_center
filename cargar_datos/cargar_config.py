import os
import json


def Config():
    ruta = os.path.join(os.path.dirname(__file__),"..", "config.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
