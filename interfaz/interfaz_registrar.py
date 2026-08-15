import customtkinter as ctk
from cargar_datos.cargar_coordinadores import Coordinadores
import os


color_fondo = "#F5F5F5"


color_tarjeta = "#FFFFFF"
color_borde = "#D9D9D9"

color_boton = "#007AFF"
color_apretado = "#005ABB"

color_selector="#66D4CF"

color_texto = "#1F2937"
color_secundario = "#6B7280"
color_primario = "#2563EB"

fuente_titulo = ("Segoe UI", 26, "bold")
fuente_subtitulo = ("Segoe UI", 14)
fuente_normal = ("Segoe UI", 12)


## Aqui vamos a llama los datos del codigo anterior, del formulario
# y vamos a imprimirlos como un resumen como una vista previa antes de imprimirlo dentro del excel

class Registrar(ctk.CTkFrame):
    def __init__(self, parent, datos, formulario):
        super().__init__(parent)

        self.parent = parent
        self.formulario = formulario

        self.datos = datos

        self.nombre_archivo = os.path.basename(datos["archivo"])
        

        self.configure(fg_color = color_fondo)

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


        self.zona_resumen = ctk.CTkLabel(
            self,
            width=350,
            height=400,
            fg_color=color_tarjeta,
            border_width=2,
            border_color=color_borde,
            corner_radius=30
        )
        self.zona_resumen.pack()
        self.zona_resumen.pack_propagate(
            False
        )

        self.texto_resumen = ctk.CTkLabel(
            self.zona_resumen,
            text="Resumen:",
            font=("Segoe UI", 16, "bold"),
            text_color=color_texto
        )
        self.texto_resumen.pack(pady = (5, 5))

        self.texto_fecha = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Fecha:",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_fecha.pack(pady=(1, 1))

        self.texto_hora = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Hora:",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_hora.pack(pady=(1, 1))

        self.texto_coordinador = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Fecha:",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_coordinador.pack(pady=(1, 1))


        self.texto_archivo = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Archivo: {self.nombre_archivo}",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_archivo.pack(pady=(1, 1))


        self.texto_curso = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Curso: {datos["curso"]} {datos["letras"]}",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_curso.pack(pady=(1, 1))

        self.texto_copias = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Copias: {datos["alumnos"]}",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_copias.pack(pady=(1, 1))

        self.texto_caras = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Caras: {datos["caras"]}",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_caras.pack(pady=(1, 1))

        self.texto_hojas = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Hojas: {datos["hojas"]}",
            font=("Segoe UI", 10, "bold"),
            text_color=color_texto
        )
        self.texto_hojas.pack(pady=(1, 1))



        self.boton_registrar = ctk.CTkButton(
            self.zona_resumen,
            text= "Registrar",
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
        
        self.boton_registrar.pack(pady=(10, 10))

    

#########################################
# Funciones no visualees
    def volver(self):
        self.destroy()
        self.formulario.pack(fill="both", expand=True)

    