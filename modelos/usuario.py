class Usuario:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def __str__(self):
        return self.usuario