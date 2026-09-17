import json
import os


class ArchivoServicio:

    def __init__(self, ruta_base="."):
        self.ruta_base = ruta_base

    def leer_json(self, archivo):
        ruta = os.path.join(self.ruta_base, archivo)

        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo_json:
            return json.load(archivo_json)

    def guardar_json(self, archivo, datos):
        ruta = os.path.join(self.ruta_base, archivo)

        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo_json:
            json.dump(
                datos,
                archivo_json,
                indent=4,
                ensure_ascii=False
            )