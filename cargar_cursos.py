import os
import json

#Funcion para cargar los cursos(en mi caso), pero los datos que quieras para calcular las copias
# Sean empleados o lo que necesites, pero claro, siguiendo la estructura del json
def cargar_cursos():

    ruta = os.path.join(os.path.dirname(__file__), "cursos.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

    
# Con esta funcion llamamos a las letras dentro de cada curso, o la variable
# que tu necesites segun la estructura de tu json. En este caso yo necesito 
# la letras de cada curso, sea A B o C segun el caso y la cantidad de alumnos.
def obtener_letras(cursos, curso):
    return cursos.get(curso, {})

