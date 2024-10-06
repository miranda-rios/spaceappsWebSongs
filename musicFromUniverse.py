from scripts.a_ImageProcessor import ImageProcessor
from scripts.b_WavelengthToMIDIConverter import WavelengthToMIDIConverter
from scripts.c_MIDIPortHandler import MIDIPortHandler


# Procesamiento de imagen
image_path = os.path.join(project_dir, "Imagenes", "3.NGC_1512.tif")
num_points = 5000
outputImage_csv = 'puntos_seleccionados.csv'  # Archivo CSV para guardar puntos
outputMIDI_csv = 'midi_notes.csv'  # Archivo que contiene las notas MIDI
threshold = 0.3

# Inicializa el procesador de imágenes y guarda los puntos en el archivo CSV
processor = ImageProcessor(image_path, threshold, num_points, (700, 1400), (5000, 25000), outputImage_csv)

# Conversión a MIDI
# Inicializa el convertidor de longitudes de onda a MIDI y guarda las notas MIDI en un archivo
midi_converter = WavelengthToMIDIConverter(outputImage_csv, outputMIDI_csv)

# Manejo de puertos MIDI y envío de notas
# Inicializa el manejador de puertos MIDI, enviando las notas desde el archivo CSV
midi_handler = MIDIPortHandler(outputMIDI_csv, 0.01, 0.2, 0.1)

# Envío de notas MIDI
midi_handler.print_output_ports()
midi_handler.send_midi_notes(outputMIDI_csv, 0.01, 0.2, 0.1)
