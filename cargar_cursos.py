import os
import json

    #Funcion para cargar los cursos(en mi caso), pero los datos que quieras para calcular las copias
    # Sean empleados o lo que necesites, pero claro, siguiendo la estructura del json
def cargar_cursos():

    ruta = os.path.join(os.path.dirname(__file__), "cursos.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
