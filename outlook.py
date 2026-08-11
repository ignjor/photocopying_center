
import os
import struct
import tempfile

import pythoncom
import win32clipboard
import win32com.server.policy


## Este codigo funciona como protocolo para outloook, para que podamos recibir los archivos
# arrastrados desde outlook sin la necesidad de tener que descargarlos y arrastrarlos al sistema de forma manual

# de todas maneras los archivos se guardan en una carpeta temporal, pero no hay necesidad de hacerlo de forma manual
# Este codigo habilita esa opción, arrastrar cosas directamente desde outlook.


CARPETA_TEMPORAL = os.path.join(
    tempfile.gettempdir(),
    "ApoyoFotocopias"
)

os.makedirs(
    CARPETA_TEMPORAL,
    exist_ok=True
)

FORMATO_GRUPO = win32clipboard.RegisterClipboardFormat(
    "FileGroupDescriptorW"
)

FORMATO_CONTENIDO = win32clipboard.RegisterClipboardFormat(
    "FileContents"
)


def obtener_nombres(data_object):

    formato = (
        FORMATO_GRUPO,
        None,
        pythoncom.DVASPECT_CONTENT,
        -1,
        pythoncom.TYMED_HGLOBAL
    )

    datos = data_object.GetData(formato).data

    cantidad = struct.unpack(
        "<I",
        datos[:4]
    )[0]

    nombres = []

    # FILEDESCRIPTORW mide 592 bytes
    tamaño = 592

    for i in range(cantidad):

        inicio = 4 + (i * tamaño)

        descriptor = datos[
            inicio:inicio + tamaño
        ]

        # cFileName comienza en el byte 72
        nombre = descriptor[72:592].decode(
            "utf-16-le",
            errors="ignore"
        )

        nombre = nombre.split(
            "\x00",
            1
        )[0]

        nombres.append(nombre)

    return nombres


def guardar_adjunto(
    data_object,
    indice,
    nombre
):

    formato = (
        FORMATO_CONTENIDO,
        None,
        pythoncom.DVASPECT_CONTENT,
        indice,
        pythoncom.TYMED_ISTREAM
    )

    datos = data_object.GetData(formato)

    stream = datos.data

    contenido = stream.Read(
        stream.Stat()[2]
    )

    ruta = os.path.join(
        CARPETA_TEMPORAL,
        nombre
    )

    with open(
        ruta,
        "wb"
    ) as archivo:

        archivo.write(contenido)

    return ruta


def obtener_archivos_outlook(data_object):

    nombres = obtener_nombres(
        data_object
    )

    archivos = []

    for indice, nombre in enumerate(nombres):

        ruta = guardar_adjunto(
            data_object,
            indice,
            nombre
        )

        archivos.append(ruta)

    return archivos


class DropTarget(
    win32com.server.policy.DesignatedWrapPolicy
):

    _reg_clsid_ = (
        "{8F0E1B2C-1B37-4C5D-9A2E-7D4B6F83A912}"
    )

    _public_methods_ = [
        "DragEnter",
        "DragOver",
        "DragLeave",
        "Drop"
    ]

    _com_interfaces_ = [
        pythoncom.IID_IDropTarget
    ]

    def __init__(self, callback):

        self.callback = callback

        self._wrap_(self)


    def DragEnter(
        self,
        data_object,
        key_state,
        point,
        effect
    ):

        return 1


    def DragOver(
        self,
        key_state,
        point,
        effect
    ):

        return 1


    def DragLeave(self):

        pass


    def Drop(
        self,
        data_object,
        key_state,
        point,
        effect
    ):

        try:

            archivos = obtener_archivos_outlook(
                data_object
            )

            self.callback(
                archivos
            )

        except Exception as error:

            print(
                f"Error con Outlook: {error}"
            )

        return 1


drop_target = None
drop_wrapper = None


def registrar_outlook_drop(
    hwnd,
    callback
):

    global drop_target
    global drop_wrapper

    drop_target = DropTarget(
        callback
    )

    drop_wrapper = pythoncom.WrapObject(
        drop_target,
        pythoncom.IID_IDropTarget,
        pythoncom.IID_IDropTarget
    )

    pythoncom.RegisterDragDrop(
        hwnd,
        drop_wrapper
    )


def cerrar_outlook_drop(hwnd):

    global drop_target
    global drop_wrapper

    try:

        pythoncom.RevokeDragDrop(
            hwnd
        )

    except Exception:
        pass

    drop_target = None
    drop_wrapper = None

