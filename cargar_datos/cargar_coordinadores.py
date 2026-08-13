import os
import json


## Aqui vamos a llamar a los cordinadores segun lo requiero, tenemos que lograr que se pueda TABEAR para escribir manual
## Así metemos cuando no sean coordinadores
def Coordinadores():
    ruta = os.path.join(os.path.dirname(__file__),"..", "coordinadores.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
