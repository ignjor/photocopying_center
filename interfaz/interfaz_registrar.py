import customtkinter as ctk
from cargar_datos.cargar_coordinadores import Coordinadores
import os

# importamos libreria para que podamos usar la fecha dentro de nuestro input de fecha, y qu
# agarre la fecha del sistema para colocar le fecha de hoy como predeteminada.
from datetime import datetime


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

        self.nombre_archivo = os.path.splitext(os.path.basename(datos["archivo"]))[0]


        # definimo la variable que va a guardar la fecha de hoy, asi la llamamos despues cuando la necesiemos llamar
        # dentro del sistema del input.
        ahora = datetime.now()
        self.fecha_actual = ahora.strftime("%d/%m/%Y")
        self.hora_actual = ahora.strftime("%H:%M")

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

        self.fecha = ctk.CTkLabel(
            self,
            text="Fecha del Registro:",
            font=("Segoe UI", 17, "bold"),
            text_color=color_secundario
        )
        self.fecha.pack(
            pady=(0, 10)
        )
        self.zona_inputfecha = ctk.CTkEntry(
            self,
            placeholder_text="dd/mm/aaaa",
            width=180,
            height=35,
            font=("Segoe UI", 13, "bold")
        )
        self.zona_inputfecha.pack(pady=(5,5))
        self.zona_inputfecha.insert(0, self.fecha_actual)
        self.zona_inputfecha.bind(
            "<KeyRelease>",
            self.actualizar_resumen
        )

        self.hora = ctk.CTkLabel(
            self,
            text="Hora del Registro: ",
            font=("Segoe UI", 17, "bold"),
            text_color=color_secundario
        )
        self.hora.pack(
            pady=(0, 10)
        )

        self.zona_inputhora = ctk.CTkEntry(
            self,
            placeholder_text="hh:mm",
            width=180,
            height=35,
            font=("Segoe UI", 13, "bold")
        )
        self.zona_inputhora.pack(pady=(5,5))
        self.zona_inputhora.insert(0, self.hora_actual)
        self.zona_inputhora.bind(
            "<KeyRelease>",
            self.actualizar_resumen
        )





# Zona completa del label de resumen, llamamos los datos de la lista datos que mandamos 
# desde el otro archivo.
        self.zona_resumen = ctk.CTkLabel(
            self,
            width=350,
            height=350,
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
            text=f"Fecha:{self.zona_inputfecha} ",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_fecha.pack(pady=(1, 1))

        self.texto_hora = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Hora: {self.zona_inputhora}",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_hora.pack(pady=(1, 1))

        self.texto_coordinador = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Fecha:",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_coordinador.pack(pady=(1, 1))


        self.texto_archivo = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Archivo: {self.nombre_archivo}",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_archivo.pack(pady=(1, 1))


        self.texto_curso = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Curso: {datos["curso"]} {datos["letras"]}",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_curso.pack(pady=(1, 1))

        self.texto_copias = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Copias: {datos["alumnos"]}",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_copias.pack(pady=(1, 1))

        self.texto_caras = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Caras: {datos["caras"]}",
            font=("Segoe UI", 13, "bold"),
            text_color=color_texto
        )
        self.texto_caras.pack(pady=(1, 1))

        self.texto_hojas = ctk.CTkLabel(
            self.zona_resumen,
            text=f"Hojas: {datos["hojas"]}",
            font=("Segoe UI", 13, "bold"),
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

            command=self.registrar
        )
        
        self.boton_registrar.pack(pady=(10, 10))

    

#########################################
# Funciones
    def volver(self):
        self.destroy()
        self.formulario.pack(fill="both", expand=True)

    # Aqui en parte vamos a hacer el evento para que cuando escribamos en lo que sea
    # Fecha y ahora se actualice al momento en el resumen, es solo visual
    def actualizar_resumen(self, event = None):
        self.texto_fecha.configure(
            text=f"Fecha: {self.zona_inputfecha.get()}"
        )
        self.texto_hora.configure(
            text=f"Hora: {self.zona_inputhora.get()}"
        )

    def registrar(self):
        fecha = self.zona_inputfecha.get()
        hora = self.zona_inputhora.get()

        #Nos falta aun la variable del coordinador
        datos_registro = {
            "fecha" : fecha,
            "hora" : hora,
            "archivo": self.nombre_archivo,
            "hojas": self.datos["cant_hojas_archivo"],
            "curso": self.datos["curso"],
            "letras": self.datos["letras"],
            "alumnos": self.datos["alumnos"],
            "caras": self.datos["caras"],
         ## Hojas no lo mandamos porque el excel tiene su propia formula   "hojas": self.datos["hojas"],
         # Tampoco mandamos la multiplicacion entre copias y hojas del doc por eso mismo.
        }
        print(datos_registro)