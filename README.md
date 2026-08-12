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

Requerimiento de la libreria para poder ver el entorno visual

Requerimiento de la libreria para poder llamar al drag and drop

Requerimiento de la libreria para poder llamar a win32


---

## Objetivos

- [x] 1. Poder leer archivos mediante el Drag and Drop desde Outlook sin tener que descargarlos y luego arrastrarlo, quesirve arrastrarlo desde Outlook, sean .pdf y los .dock mediante una COM de Word

- [x] 2. Interfaz visual en CustomTkinter con drag and drop con cualquier archivo sea .pdf o .docx desde el correo sin necesidad de guardarlo.

- [ ] 3. Mostrar dentro de la interfaz visual y poder seleccionar la cantidad de copias segun el curso que seleccionemos, sea A B o C. Calcular automaticamente

- [ ] 4. Presentar dentro del sistema el calculo para el total de copias, dividirlo segun la cantidad de caras de la impresión.

- [ ] 5. Registrar en excel los datos de las variables rescatadas exactamente en las columnas y filas requeridas con orden correlativo

- [ ] 6. Lo mismo con la fecha, hora, coordinadora. Optimizaciones finales y testeo.

---
## Historial 2026

El historial recopia los avances del sistema durante su periodo inicial de desarrollo, el plazo objetivo del desarrollo son de 2 semanas.

### Lunes 10 de Agosto

- Desarrollo de las funciones iniciales del proyecto, el sistema lee las paginas sea de pdf o word mediante LibreOffice, aun no se desarrolla entorno visual.

- Se desarrollo el .json con los cursos completos, aun no se importa ni se implementa dentro del proyecto.

### Martes 11 de Agosto

- Se desecho libreoffice, se utiliza una COM de Word, agiliza el desarrollo y la instalación del proyecto, la unica limitación es tener instalado Office.

- Se desarrollo un entonro visual con CustomTkinter, ademas usamos otra libreria para usar el Drag and Drop desde outlook, se desarrollo un .py para poder arrastrar los archivos directamente desde outlook al sistema, se guardan en uan carpeta temporal.

- Agregamos ventana incial para formulario con la cantidad de páginas del documento y el nombre del archivo

- Se agrego un boton para volver a la ventana Drag and Drop inicial para Scannear mas archivos, de esa forma aprovechamos que aun no registra en excel, pero para saber la cantidad de paginas de forma rapida sin neceidad de abrirlo,

- Se agrego la funcion para importar el .json con todos los cursos.

- Se agrego el Label con los cursos importados, solo importa la key de los cursos, sin las letras.

### Miercoles 12 de Agosto

- Se agrego la estructura para llamar las letras dentro de otro archivo e importarlas dentro del formulario.

- Se agrego la estructura para ver visualmente las letras de cada curso y sumar sus resultados, se imprime en consola falta que lo hagas visual.

- Se agrego la funcion para que puedas ademas de sumar, multiplicar por la cantidad de paginas del documento, tambien es por consola, falta agregar que puedas elegir 1 o 2 caras y se divida por el resultado del total de hojas.