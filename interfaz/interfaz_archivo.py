import customtkinter as ctk
from tkinterdnd2 import TkinterDnD
import pythoncom

from funciones.documentos import obtener_cantidad_hojas
from interfaz.interfaz_formDoc import Formulario
from funciones.outlook import (registrar_outlook_drop, cerrar_outlook_drop)


ctk.set_ctk_parent_class(TkinterDnD.Tk)

# Nuestros estilos, podemos ir agregando mas a medida de que lo necesitemos
# la idea es que por ej todas las interfaces sean separadas para no tener archivos grandes

color_fondo = "#F5F5F5"
color_tarjeta = "#FFFFFF"
color_borde = "#D9D9D9"

color_texto = "#1F2937"
color_secundario = "#6B7280"
color_primario = "#2563EB"

fuente_titulo = ("Segoe UI", 26, "bold")
fuente_subtitulo = ("Segoe UI", 14)
fuente_normal = ("Segoe UI", 12)


## Definimos la clase para la funcionalidad de esta clase
class Aplicacion(ctk.CTk):

    # Definimos lo que necesitamos para llamar a lo visual
    def __init__(self):
        super().__init__()

        # Y llamamos self que podria definirse como "a esta ventana"
        self.title("Centro de Fotocopias")

        # Le ponemos la geomtria inicial que va a tener la ventana al abrir la ventana
        self.geometry("500x500")

        self.minsize(500, 400)

        self.resizable(False, True)

        self.configure(fg_color = color_fondo)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

        self.crear_interfaz()

        #Se inicia el OLE pero no tengo idea es el OLE
        pythoncom.OleInitialize()

        self.after(
            100, self.registrar_outlook
        )


    def crear_interfaz(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="Centro de Fotocopias",
            font=fuente_titulo,
            text_color=color_texto
        )
        self.titulo.pack(pady=(60, 10))


        self.subtitulo = ctk.CTkLabel(
            self,
            text="Arrastra un archivo para escanearlo",
            font=fuente_subtitulo,
            text_color=color_secundario

        )
        self.subtitulo.pack(pady=(0, 35))


        self.zona_archivo = ctk.CTkLabel(
            self,
            width=350,
            height=220,
            fg_color=color_tarjeta,
            border_width=2,
            border_color=color_borde,
            corner_radius=30
        )
        self.zona_archivo.pack()
        self.zona_archivo.pack_propagate(
            False
        )


        self.icono = ctk.CTkLabel(
            self.zona_archivo,
            text="📄",
            font=("Segoe UI", 40)
        )
        self.icono.pack(pady=(40, 10))


        self.texto_arrastrar = ctk.CTkLabel(
            self.zona_archivo,
            text="Suelta aquí el archivo",
            font=("Segoe UI", 16, "bold"),
            text_color=color_texto
        )
        self.texto_arrastrar.pack()

        self.texto_formato = ctk.CTkLabel(
            self.zona_archivo,
            text=".pdf o .docx",
            font=fuente_normal,
            text_color=color_secundario
        )
        self.texto_formato.pack(pady=(8, 0))


    def registrar_outlook(self):

        registrar_outlook_drop(
            self.zona_archivo.winfo_id(),
            self.archivo_outlook
        )
        print("Arrastre funciona correctamente")


    def archivo_outlook(self, archivos):

        if not archivos:
            return

        archivo = archivos[0]

        print("Archivo recibid desde oulook")
        print(archivo)

        self.procesar_archivo(archivo)


    def procesar_archivo(self, archivo):
        
        print(f"Archivo recibido {archivo}")

        try:
            cantidad = obtener_cantidad_hojas(
                archivo
            )
            print(f"Cantidad de hojas: {cantidad}")

        except Exception as error: print(f"Error: {error}")

    def mostrar_formulario(self, cantidad, archivo):

        self.titulo.pack_forget()
        self.subtitulo.pack_forget()
        self.zona_archivo.pack_forget()

        self.formulario = Formulario(
            self,
            cantidad,
            archivo
        )

        self.formulario.pack(
            fill="both",
            expand=True
        )

    def procesar_archivo(self, archivo):

        print(f"Archivo recibido {archivo}")

        try:
            cantidad = obtener_cantidad_hojas(
                archivo
            )

            print(f"Cantidad de hojas: {cantidad}")

            self.mostrar_formulario(cantidad, archivo)

        except Exception as error:
            print(f"Error: {error}")



    def cerrar_aplicacion(self):

        try:
            cerrar_outlook_drop(
                self.zona_archivo.winfo_id()
            )

        except Exception: pass

        try: pythoncom.OleInitialize()

        except Exception: pass

        self.destroy()

    def mostrar_interfaz(self):
        self.titulo.pack(pady=(60, 10))
        self.subtitulo.pack(pady=(0, 35))
        self.zona_archivo.pack()


        
