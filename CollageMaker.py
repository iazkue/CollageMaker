import os
from PIL import Image

# === CONFIGURACIÓN ===
carpeta_imagenes = "argazkiak"  # Carpeta donde están tus imágenes
output = "collage_final.jpg"   # Nombre del archivo de salida
columnas = 6                    # Número de columnas del collage
tamano_celda = (1984, 1488)      # (ancho, alto) de cada imagen en el collage
espaciado = 10                 # Espacio entre imágenes

# === CARGAR Y REDIMENSIONAR TODAS LAS IMÁGENES ===
imagenes = []
for archivo in sorted(os.listdir(carpeta_imagenes)):
    if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
        ruta = os.path.join(carpeta_imagenes, archivo)
        img = Image.open(ruta).convert("RGB")
        img = img.resize(tamano_celda, Image.LANCZOS)
        imagenes.append(img)

if not imagenes:
    raise ValueError("No se encontraron imágenes en la carpeta especificada.")

# === CALCULAR TAMAÑO DEL COLLAGE ===
filas = (len(imagenes) + columnas - 1) // columnas
ancho_total = columnas * tamano_celda[0] + (columnas - 1) * espaciado
alto_total = filas * tamano_celda[1] + (filas - 1) * espaciado

# === CREAR COLLAGE ===
collage = Image.new("RGB", (ancho_total, alto_total), color=(0, 0, 0))

for idx, img in enumerate(imagenes):
    col = idx % columnas
    fila = idx // columnas
    x = col * (tamano_celda[0] + espaciado)
    y = fila * (tamano_celda[1] + espaciado)
    collage.paste(img, (x, y))

# === GUARDAR COLLAGE ===
collage.save(output, quality=95)
print(f"✅ Collage guardado en: {output}")
