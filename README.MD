# <center> Conversor de canciones a formato mp3 </center>

![Logo Aplicación para convertir canciones](./logo_conversor_canciones.png)


# Requisitios y características

## Windows

Para ejecutar la aplicación en Windows, solo habría que descargar las depedencias con el instalador de paquetes pip

```bash
cmd
pip install pytube
pip install Pyllow

```

## Linux
Para Linux con la distro de Ubuntu, hay que hacer un par de procesos más, como generar un virtualenv para correr nuestro proyecto.

Los pasos serían:

### Instalar virtualenv

```bash 
bash
pip install virtualenv
```

### Crear nuestro entorno virtual

Luego en el directorio de nuestro proyecto, crearemos un directorio donde se almacene el entorno virtual:

```bash
bash
virtualenv downloader_audios
```

### Activación del entorno virtual

El nombre del entorno virtual es lo de menos, pero con él, podremos instalar las dependencias con pip y, luego, como si fuera node, instalar todas las dependencias tras activar el entorno virtual:

```bash
bash
source downloader_audios/bin/activate
```

### Instalar dependencias

Por fin, tras haber instalado previamente las dependencias con los comandos que mencionamos anteriormente, podríamos instalar las dependencias en el proyecto.

```bash
bash
pip install requests
```

# Uso de la aplicación

La app es muy sencilla y está diseñada con Tkinter, con las limitaciones que ofrece en temas de diseño. Hay otras librerías para crear aplicaciones de escritorio como PyQt5, pero para el propósito de esta aplicación Tkinter basta y sobra.

## Abrir aplicación 

Se puede hacer desde consola ejecutando: 

```bash
python3 main.py
```

Así se abrirá la interfaz de Tkinter y solo tendremos que introducir el enlace de la canción y vídeo que queramos descargar y este se guardará en el fichero songs.


# Incidencias

Desde hace un tiempo, a la hora de descargar la canción la petición devuelve un error 403, por lo que habría que esperar actualizaciones de la librería o de la plataforma de YouTube. Si hubieran actualizaciones, se corregiría en la siguiente versión

