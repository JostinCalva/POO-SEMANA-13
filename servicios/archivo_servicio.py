import json
import os


class ArchivoServicio:
    def __init__(self, carpeta_datos):
        self.carpeta_datos = carpeta_datos

    def leer_json(self, nombre_archivo):
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)

        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)