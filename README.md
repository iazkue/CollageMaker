# CollageMaker

CollageMaker es un script en Python que genera un collage a partir de un conjunto de imágenes. 

## Requisitos

- Python 3.x
- Biblioteca [Pillow](https://python-pillow.org/) (instalable con `pip install pillow`)

## Uso

1. Coloca las imágenes que deseas usar en la carpeta `argazkiak`.
2. Configura los parámetros en el archivo `CollageMaker.py`:
   - `carpeta_imagenes`: Carpeta donde están las imágenes.
   - `output`: Nombre del archivo de salida.
   - `columnas`: Número de columnas en el collage.
   - `tamano_celda`: Tamaño de cada imagen en el collage (ancho, alto).
   - `espaciado`: Espacio entre las imágenes.
3. Ejecuta el script:
   ```bash
   python CollageMaker.py