from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

        self.productos = []
        self.usuarios = []

        self.cargar_productos()
        self.cargar_usuarios()

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json("productos.json")

        self.productos = [
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            )
            for producto in datos
        ]

    def cargar_usuarios(self):
        datos = self.archivo_servicio.leer_json("usuarios.json")

        self.usuarios = [
            Usuario(
                usuario["usuario"],
                usuario["contrasena"]
            )
            for usuario in datos
        ]

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return True

        return False

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def cantidad_productos(self):
        return len(self.productos)

    def cantidad_usuarios(self):
        return len(self.usuarios)