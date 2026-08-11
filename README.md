# (In Development)


# School Photocopy Center (ES) 

Sistema para calcular hojas de documentos de forma rapida .pdf .docx desde OUTLOOK sin tener que descargar los archivos y almacenarlas dentro de un excel de forma rapida y ordenada.

## Instrucciones de instalación

El sistema requiere tener Office Word instalado en la computadora para leer las páginas de los archivos Word sin abrirlos.


Instala los requerimientos (Aún no desarrollamos una interfaz visual de CustomTkinter) (en desarrollo)

## Requerimientos

(requerimientos .txt en desarrollo)

Requerimiento de la libreria para poder leer y escribir dentro del Excel.
```bash
pip install openpyxl
```

Requerimiento de la libreria para poder leer los pdf.
```bash
pip install PyMuPDF
```

---

## Objetivos

- [x] 1. Poder leer archivos mediante el Drag and Drop desde Outlook sin tener que descargarlos y luego arrastrarlo, quesirve arrastrarlo desde Outlook, sean .pdf y los .dock mediante una COM de Word

- [x] 2. Interfaz visual en CustomTkinter con drag and drop con cualquier archivo sea .pdf o .docx desde el correo sin necesidad de guardarlo.

- [ ] 3. Mostrar dentro de la interfaz visual y poder seleccionar la cantidad de copias segun el curso que seleccionemos, sea A B o C. Calcular automaticamente

- [ ] 4. Presentar dentro del sistema el calculo para el total de copias, dividirlo segun la cantidad de caras de la impresión.

- [ ] 5. Registrar en excel los datos de las variables rescatadas exactamente en las columnas y filas requeridas con orden correlativo

- [ ] 6. Lo mismo con la fecha, hora, coordinadora. Optimizaciones finales y testeo.