import os
import fitz

import win32com.client

word_app = None

# Funcion para inciar word cuando lo necesitemos
def iniciar_word():

    global word_app

    if word_app is not None:

        try:
            _= word_app.Version
            return

        except:
            cerrar_word()

    print("Word se esta iniciando Correctamente...")

    word_app = win32com.client.DispatchEx("Word.Application")

    word_app.Visible = False
    word_app.DisplayAlerts = 0

    print("Word se ejecuto correctamente") 

# Cerramos Word cuando el sistema ya no lo requiera
def cerrar_word():
    global word_app

    if word_app is None:
        return

    print("Cerrando Word...")

    try:
        word_app.Quit()

    except Exception: pass

    word_app = None

# Contamos páginas del word con la funcion de fitz de pdf
def contar_paginas_pdf(archivo):

    documento = fitz.open(archivo)

    try:

        cantidad_paginas = len(documento)

        return cantidad_paginas

    except: documento.close()

# Contamos las páginas con el Repaginatey ComputeStatistics de Word COM, lo ponemos que sea solo lectura
# y ademas que no se muestre en pantalla y que tampoco muestre mensajes en pantalla de word
def contar_paginas_word(archivo):

    iniciar_word()

    documento = None

    try:
        documento = word_app.Documents.Open(
            FileName = os.path.abspath(archivo),
            ReadOnly = True,
            AddToRecentFiles = False,
            Visible = False
        )

        documento.Repaginate()

        cantidad_paginas = documento.ComputeStatistics(2)
        return cantidad_paginas

    except Exception as error:
        print(f"Error en word: {error}")

        cerrar_word()
        raise

    finally:
        if documento is not None:
            try:
                documento.Close(

                    SaveChanges = False
                )

            except Exception: pass

# Aqui vemos como es el archivo que llego para saber a que funcion lo tenemos que tirar, a pdf o a word.
def obtener_cantidad_hojas(archivo):

    if not os.path.isfile(archivo):
        raise FileNotFoundError("El archivo no existe")

    extension = os.path.splitext(archivo)[1].lower()

    if extension == ".pdf":
        cantidad = contar_paginas_pdf(archivo)

        return cantidad

    elif extension == ".docx":
        return contar_paginas_word(archivo)

    else : raise ValueError("El archivo es imcompatible")