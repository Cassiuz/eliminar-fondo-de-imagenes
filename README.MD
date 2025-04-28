# Procesado de imágenes con Python: creando un eliminador de fondos desde cero

## Sesión 1
1. Creamos nuestro proyecto con un main.py
2. En el main.py creamos el programa principal y le pasamos como argumento el directorio de la imagen a procesar. Los argumentos los procesamos en una función independiente. Ej: python -m main.py -f /ruta/a/image.png
3. Creamos los tests para comprobar que la función de gestión de argumentos funciona corectamente con o sin el argumento de la ruta.

## Sesión 2
1. Añadimos una función para leer la ruta pasada por parámetro. Debe identificar si existe y, si lo hace, almancenar los datos en un array de bytes (binario).
2. Una vez que tenemos los datos en binario, identificamos que tipo de archivo es a través de esa información (por ahora, solo identificamos y procesaremos PNGs).
3. Creamos una función para convertir los datos binarios a un array de pixeles en el caso de los archivos PNG, y si recibimos ese tipo de archivo lo convertimos.

## Sesión 3
