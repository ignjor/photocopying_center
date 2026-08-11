import customtkinter as ctk

color_fondo = "#F5F5F5"
color_tarjeta = "#FFFFFF"
color_borde = "#D9D9D9"

color_texto = "#1F2937"
color_secundario = "#6B7280"
color_primario = "#2563EB"

fuente_titulo = ("Segoe UI", 26, "bold")
fuente_subtitulo = ("Segoe UI", 14)
fuente_normal = ("Segoe UI", 12)


class Formulario(ctk.CTkFrame):

    def __init__(self, master, cantidad_hojas, archivo):
        super().__init__(master)

        self.cantidad_hojas = cantidad_hojas

        self.texto = ctk.CTkLabel(
            self,
            text=f"Cantidad de hojas: {self.cantidad_hojas}",
            font=("Segoe UI", 20, "bold"),
            text_color=color_texto
        )

        self.texto.pack(
            pady=(60, 10)
        )

        self.configure(fg_color = color_fondo)

        self.archivo = archivo

        self.nombre = ctk.CTkLabel(
            self,
            text=f"{self.archivo}",
            font=("Segoe UI", 10),
            text_color=color_secundario
        )
        self.nombre.pack(
            pady=(0, 10)
        )

        self.boton_curso = ctk.CTkRadioButton(
            self,
            width=200,
            height=50,
            fg_color=color_tarjeta,
            border_color=color_borde,
            corner_radius=50
        )
        self.boton_curso.pack()
        self.boton_curso.pack_propagate(
            False
        )


        



