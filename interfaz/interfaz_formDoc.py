import customtkinter as ctk
import os

from cargar_datos.cargar_cursos import cargar_cursos, obtener_letras


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

        # Aqui llamamos a la funciones que importamos desde nuestro otro archivo
        self.cursos = cargar_cursos()

        # Guardamos la letras seleccionadas dentor de una lista, así podemos listar y guardar A B o C segun el caso del curso
        # Aqui las letras
        self.letra_seleccionada = []

        # En esta variable vamos a guardar la suma completa de los alumnos selecciados, ese numero lo calculamos
        # segun la cantidad de las letras que guardamos.

        #Aqui guardamos todos los alumnos seleccionados
        self.cantidad_alumnos = 0

        # Aqui vamos a guardar la cantidad de hojas total que vamos a usar, eso lo vamos a hacer multipicando las paginas del achivo
        # (que rescatamos del interfaz_archivo, esa variable cantidad_hojas) multiplicada con la variable anterior
        # nos falta hacer que podamos dividirlo por 1 o 2 caras, pero luego.
        self.cantidad_hojas = cantidad_hojas

        # Aqui guardas la suma total, NO la mandes para el excel porque el excel deberia hacer la formula solito, si no es tu caso, no te preocupes mandalo nomas
        # pero yo no lo agrego
        self.total_hojas = 0

        # Caras, aqui guardamos si la impresion es por 1 o ambas caras
        # Siendo claro, predeterminado 1 para evitar que sistema divida por 0
        self.total_caras = 1

        self.hojas = 0


        
        
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

        cursos = list(self.cursos.keys())
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
        self.selector.set(cursos[0])



        self.frame_letras = ctk.CTkFrame(
            self,
            fg_color="transparent",
            
            
        )
        self.frame_letras.pack(pady=(0,5), padx = (5))
        ## Aqui definimos la variable como set en 0, es decir el priemro de la
        # lista del json, en nuestro caso, en prekinder, de esa forma las letras
        # no esperan a recibir un dato para aprecer, como tenemos el set en 0
        # aparecen como si hubieramos selecionado el primer dato, asi evitamos errores
        # visuales cuando pongamos mas cosas abajo
        self.curso_seleccionado(cursos[0])


        self.copias = ctk.CTkLabel(
            self,
            text=f"Total de Copias: {self.cantidad_alumnos}",
            font=("Segoe UI", 17, "bold"),
            text_color=color_secundario
        )

        self.copias.pack(
            pady=(0, 10)
        )

        # Definimos la variable para guardar las caras, y los radio boton van juntitos, y llaman a la funcion
        # del selector para cambiar automaticamente, una chulada papá
        self.caras_selector = ctk.IntVar(value=1)
        self.radio1 = ctk.CTkRadioButton(
            self,
            text = "Una Cara",
            variable = self.caras_selector,
            value=1,
            font=("Segoe UI", 13, "bold"),
            command=self.actualizar_seleccion
        )
        self.radio1.pack(pady=5)

        self.radio2 = ctk.CTkRadioButton(
            self,
            text = "Ambas Caras",
            variable = self.caras_selector,
            value=2,
            font=("Segoe UI", 13, "bold"),
            command=self.actualizar_seleccion
        )
        self.radio2.pack(pady=5)


        self.cant_total_hojas = ctk.CTkLabel(
            self,
            text=f"Total de Copias: {self.hojas}",
            font=("Segoe UI", 17, "bold"),
            text_color=color_secundario
        )

        self.cant_total_hojas.pack(
            pady=(0, 10)
        )

        self.boton_siguiente = ctk.CTkButton(
            self,
            text= "Siguiente",
            font=("Segoe UI", 15, "bold"),
            height= 35,
            width=70,

            text_color=color_fondo,
            fg_color=color_boton,
            hover_color=color_apretado,
            corner_radius=40,
            border_color=color_secundario,

            command=self.siguiente
        )
        
        self.boton_siguiente.pack(pady=(10, 10))

        self.mensaje_error = ctk.CTkLabel(
            self,
            text="Selecciona un curso para continuar",
            font=("Segoe UI", 17, "bold"),
            text_color=color_primario
        )





################################################
#Funciones que van fuera de lo visual.

    # Aqui guardamos todas las funciones respetivasa llamar al curso y la matematica al elegir letra, se imprime en la consol
    # Falta imprimirlo logicamente en pantalla obvio.
    def curso_seleccionado(self, curso):
        x = self.cursos[curso]
        print(x)  

        self.letra_seleccionada = []
        self.cantidad_alumnos = 0

        for widget in self.frame_letras.winfo_children():
            widget.destroy()

        letras = obtener_letras(self.cursos, curso)
        self.checkboxes_letras = {}

        for letra in letras:

            checkbox = ctk.CTkCheckBox(
                self.frame_letras,
                text=f"{letra} - ({self.cursos[curso][letra]} alumnos)",
                font=("Segoe UI", 13, "bold"),
                fg_color=color_boton,
                corner_radius=30,
                
                command=self.actualizar_seleccion
                
            )

            checkbox.pack(side="top", pady=5, anchor = "center")
            self.checkboxes_letras[letra] = checkbox

    def actualizar_seleccion(self):
        self.letra_seleccionada = []
        self.cantidad_alumnos = 0

        for letra, checkbox in self.checkboxes_letras.items():

            if checkbox.get() == 1:
                self.letra_seleccionada.append(letra)
                self.cantidad_alumnos += self.cursos[self.selector.get()][letra]

        self.total_hojas = self.cantidad_alumnos * self.cantidad_hojas
        self.hojas = self.total_hojas / self.caras_selector.get()

        self.copias.configure(text=f"Total de Copias: {self.cantidad_alumnos}")
        self.cant_total_hojas.configure(text = f"Total de Copias: {self.hojas}")
        print(self.cantidad_alumnos)
            
        print(self.letra_seleccionada)
        print(self.total_hojas)
        print(self.hojas)
                


    def volver(self):
        self.destroy()
        self.parent.mostrar_interfaz()

    # Creamos el boton siguiente, lo que hacemos es mandar tooodos los datos que necesitamos
    # a la otra ventana para registrar en el excel, ya eso es mas facil porque ya tenemos todos los datos.
    def siguiente(self):
        datos = {
            "archivo": self.archivo,
            "curso": self.selector.get(),
            "letras": self.letra_seleccionada,
            "alumnos": self.cantidad_alumnos,
            "hojas": self.hojas,
            "caras": self.caras_selector.get()
        }
        print(datos)
    # Hacemos que cuando letras este vacio, no pase a la sieguiente pagina hasta que selecione una letra por lo menos
    
        if len(datos["letras"]) == 0:
           self.mensaje_error.pack(pady=(0, 10))
           return

    # Si hay letra pasamos a la siguiente ventana pasandole los datos, pero no la destruimos, por si tenemos que volver
    # despues.
        self.pack_forget()
        self.parent.mostrar_registrar(datos, self)

        

        



