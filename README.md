# Stickers Flotantes

## Descripción
Stickers Flotantes es una aplicación simple que te permite mostrar imágenes transparentes y flotantes en tu escritorio de Linux. La aplicación admite formatos PNG y GIF, lo que te permite personalizar tu escritorio con stickers animados o estáticos.

## Características
- **Flotante y Transparente**: Los stickers aparecen como ventanas flotantes sin bordes, lo que permite una integración perfecta con tu entorno de escritorio.
- **Soporta PNG y GIF**: Puedes usar tanto imágenes estáticas (PNG) como imágenes animadas (GIF) como stickers.

## Cómo Funciona
La aplicación utiliza PyQt5 para crear ventanas transparentes que muestran las imágenes especificadas. Las imágenes se pueden mover por la pantalla, y los GIF se animarán automáticamente.

### Ejecutando la Aplicación
Para ejecutar la aplicación, puedes usar el script de shell proporcionado `OpenStickers.sh`, que lanza múltiples stickers a la vez. El script incluye los siguientes comandos:

```bash
#!/bin/bash
python3 show_sticker.py fire.gif &
python3 show_sticker.py hello.gif &
python3 show_sticker.py ladybug.gif &
python3 show_sticker.py penguin.gif &
python3 show_sticker.py sun.gif &
python3 show_sticker.py cat.png &
python3 show_sticker.py fence.png &
python3 show_sticker.py flowers.png &
python3 show_sticker.py tree.png &
```

### Cerrar todos los Stickers

```bash
pkill -f show_sticker.py
```

### Personalizando los Stickers
Para personalizar los stickers:
1. Agrega tus propias imágenes (PNG o GIF) al directorio del proyecto.
2. Modifica el script `OpenStickers.sh` para incluir tus archivos de imagen.
3. Ejecuta el script para ver tus stickers personalizados en el escritorio.

## Requisitos
- Python 3
- PyQt5

## Instalación
Puedes instalar las dependencias requeridas usando pip:

```bash
pip install PyQt5
```

## Ejemplos

Video de ejemplo con los recursos en GitHub (imagines sin derechos de autor):

https://github.com/user-attachments/assets/1756a14b-2507-4c83-b67d-dae1fa4c9db2

Video con imagenes de un uso real combinado (Star Wars y HTTYD):

https://github.com/user-attachments/assets/bb985b2b-1068-4e59-8a70-8d498d558ab8

(Todos los elementos se pueden mover arrastrando)
