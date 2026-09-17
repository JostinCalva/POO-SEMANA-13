from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

        self.productos = []
        self.usuarios = []

        self.cargar_productos()
        self.cargar_usuarios()

    # =========================
    # PRODUCTOS
    # =========================

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json(
            "datos/productos.json"
        )

        self.productos = []

        for dato in datos:
            producto = Producto(
                dato["codigo"],
                dato["nombre"],
                dato["precio"],
                dato["stock"]
            )

            self.productos.append(producto)

    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append(producto.to_dict())

        self.archivo_servicio.guardar_json(
            "datos/productos.json",
            datos
        )

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if str(producto.codigo) == str(codigo):
                return producto

        return None

    def registrar_producto(self, codigo, nombre, precio, stock):

        if not codigo:
            raise ValueError("El código es obligatorio.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if self.buscar_producto(codigo) is not None:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser numérico.")

        try:
            stock = int(stock)
        except (ValueError, TypeError):
            raise ValueError(
                "El stock debe ser un número entero."
            )

        if precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self.productos.append(producto)
        self.guardar_productos()

        return "Producto registrado correctamente."

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio,
        stock
    ):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError("Producto no encontrado.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser numérico.")

        try:
            stock = int(stock)
        except (ValueError, TypeError):
            raise ValueError(
                "El stock debe ser un número entero."
            )

        if precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock

        self.guardar_productos()

        return "Producto actualizado correctamente."

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError("Producto no encontrado.")

        self.productos.remove(producto)
        self.guardar_productos()

        return "Producto eliminado correctamente."

    # =========================
    # USUARIOS
    # =========================

    def cargar_usuarios(self):

        datos = self.archivo_servicio.leer_json(
            "datos/usuarios.json"
        )

        self.usuarios = []

        for dato in datos:

            usuario = Usuario(
                dato["identificacion"],
                dato["nombre"],
                dato["usuario"],
                dato["password"]
            )

            self.usuarios.append(usuario)

    def validar_acceso(self, usuario, password):

        usuario = str(usuario).strip()
        password = str(password).strip()

        for usuario_registrado in self.usuarios:

            usuario_guardado = str(
                usuario_registrado.usuario
            ).strip()

            password_guardada = str(
                usuario_registrado.password
            ).strip()

            if (
                usuario_guardado == usuario
                and
                password_guardada == password
            ):
                return usuario_registrado

        return None