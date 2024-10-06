# Proyecto: WebbSounds

Este proyecto, desarrollado por los integrantes del semillero de astronomía en el marco del evento NASA Space Apps 2024, tiene como objetivo convertir datos de imágenes astronómicas en notas musicales. Utilizando técnicas de procesamiento de imágenes y análisis espectral, se generan puntos muestreados de imágenes y se transforman longitudes de onda en notas MIDI, que son enviadas a través de puertos MIDI para ser reproducidas.

## Integrantes del Proyecto
- Lina Alejandra Gonzalez-Ramirez
- Juan Steven Cardona-Grisales
- Daniel Pino-Roman
- Ramón Andrés Gómez-Olarte
- Froilan Esteban Moreno-Galeano
- Liz Andrea Zuñiga-Ballesteros

## Librerías Requeridas

Para ejecutar este código, necesitas instalar las siguientes bibliotecas en Python:

```bash
pip install numpy opencv-python pandas mido keyboard
```

Uso del Código

  Preparar el Entorno:
        Asegúrate de que las bibliotecas requeridas están instaladas.

  Estructura de Archivos:
        Coloca el archivo de imagen (por ejemplo, NGC 7496.tif) en el directorio Imagenes.

  Ejecutar el Código Principal:
        El código principal, llamado musicFromUniverse.py, gestiona el flujo de ejecución. Asegúrate de que la estructura de directorios sea la siguiente:

```bash
/project_directory
├── /scripts
│   ├── a_ImageProcessor.py
│   ├── b_WavelengthToMIDIConverter.py
│   └── c_MIDIPortHandler.py
├── /Imagenes
│   └── NGC 7496.tif
└── musicFromUniverse.py
```

Configurar Parámetros:

Edita las variables en musicFromUniverse.py según sea necesario:
        image_path: Ruta de la imagen.
        num_points: Número de puntos a muestrear.
        outputImage_csv: Nombre del archivo CSV para guardar los puntos.
        outputMIDI_csv: Nombre del archivo CSV para guardar las notas MIDI.
        threshold: Umbral para la máscara de luz.

## Ejecutar el Programa:

Corre el archivo musicFromUniverse.py en tu terminal:

```bash
python musicFromUniverse.py
```
Interacción con el MIDI:
        Las notas MIDI se enviarán automáticamente a través de los puertos MIDI configurados. Puedes detener la ejecución presionando la tecla Esc.

## Posibles Errores y Soluciones

*Error: "ModuleNotFoundError"*

  Descripción: Una de las bibliotecas requeridas no está instalada.
  Solución: Asegúrate de que todas las bibliotecas estén instaladas ejecutando:
 ```bash
 pip install numpy opencv-python pandas mido keyboard
 ```
*Error: "FileNotFoundError"*

  Descripción: El archivo de imagen o CSV no se encuentra en la ruta especificada.
  Solución: Verifica que la ruta del archivo de imagen y los nombres de los archivos CSV sean correctos.

*Error: "MIDI port not found"*

  Descripción: Los puertos MIDI especificados no están disponibles.
  Solución: Asegúrate de que los puertos MIDI estén configurados correctamente y que el software de MIDI (como loopMIDI) esté funcionando.

Error: "Keyboard interrupt"

  Descripción: El programa se detiene inesperadamente.
  Solución: Asegúrate de que no se estén enviando mensajes MIDI a un dispositivo que no puede recibirlos o presiona Esc para detener la ejecución de manera controlada.


