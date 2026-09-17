class Usuario:

    def __init__(
        self,
        identificacion,
        nombre,
        usuario,
        password
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.password = password

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }