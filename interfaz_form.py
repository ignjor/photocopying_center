import customtkinter as ctk
import os

from cargar_cursos import cargar_cursos


color_fondo = "#F5F5F5"
color_tarjeta = "#FFFFFF"

color_boton = "#007AFF"
color_apretado = "#005ABB"

color_selector="#66D4CF"

color_borde = "#8D8B8B"

color_texto = "#1F2937"
color_secundario = "#6B7280"
color_primario = "#2563EB"

fuente_titulo = ("Segoe UI", 26, "bold")
fuente_subtitulo = ("Segoe UI", 14)
fuente_normal = ("Segoe UI", 12)



class Formulario(ctk.CTkFrame):
    def __init__(self, parent, cantidad_hojas, archivo):
        super().__init__(parent)

        self.parent = parent
        self.cursos = cargar_cursos()
        

        
        self.configure(fg_color = color_fondo)

        self.cantidad_hojas = cantidad_hojas

        # Aquí vamos a definir un boton para volver al escanner de documentos por si nos equivocamos
        # o no es necesario.
        self.boton_volver = ctk.CTkButton(
            self,
            text= "Volver",
            font=("Segoe UI", 15, "bold"),
            height= 35,
            width=70,

            text_color=color_fondo,
            fg_color=color_boton,
            hover_color=color_apretado,
            corner_radius=40,
            border_color=color_secundario,

            command=self.volver
        )
        
        self.boton_volver.pack(anchor="w", padx=20, pady=(10, 10))

        # Y aqui quize llamar al nombre del archivo pero termine llamando a la ruta completa desde la carpeta
        # temporal que es donde se guarda, nada que hacer jasdja.
        self.archivo = archivo

        self.nombre = ctk.CTkLabel(
            self,
            text=f"{os.path.basename(archivo)}",
            font=("Segoe UI", 20, "bold"),
            text_color=color_texto
        )
        self.nombre.pack(
            pady=(10, 10)
        )

        # Definimos el texto inicial que nos va a decir la cantidad de hojas, lo llamamos desde la funcion anterior.
        self.texto = ctk.CTkLabel(
            self,
            text=f"Hojas: {self.cantidad_hojas}",
            font=("Segoe UI", 17, "bold"),
            text_color=color_secundario
        )

        self.texto.pack(
            pady=(0, 10)
        )


        #Este ComboBox es para llamar al selector
        self.selector = ctk.CTkOptionMenu(
            self,
        #Con values colocamos los valores, en este caso yo llamo las Keys del json
        # que son los cursos sin las letras
            values = list(self.cursos.keys()),
            width=100,
            height=40,

            corner_radius=30,

            fg_color=color_boton,
            text_color=color_fondo,
            font=("Segoe UI", 13, "bold"),
            dropdown_font=("Segoe UI", 13),

            button_hover_color=color_boton,
            button_color=color_boton,
            command=self.curso_seleccionado

        )
        self.selector.pack(pady=(20,20))


        self.letras = ctk.CTkButton


    
    def curso_seleccionado(self, curso):
        letra = self.cursos[curso]
        print(letra)  









    def volver(self):
        self.destroy()
        self.parent.mostrar_interfaz()
        

        

        



