import tkinter as tk
from tkinter import ttk


class MainView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        cerrar_sesion
    ):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Panel principal - Restaurante App",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=10)

        resumen = ttk.Label(
            self.frame,
            text=(
                f"Productos registrados: "
                f"{self.restaurante_servicio.cantidad_productos()}    |    "
                f"Usuarios registrados: "
                f"{self.restaurante_servicio.cantidad_usuarios()}"
            )
        )
        resumen.pack(pady=10)

        botones = ttk.Frame(self.frame)
        botones.pack(pady=10)

        ttk.Button(
            botones,
            text="Productos",
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            botones,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            botones,
            text="Ventas (pendiente)",
            command=self.ventas_pendientes
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            botones,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).grid(row=0, column=3, padx=5)

        self.contenido = ttk.Frame(self.frame)
        self.contenido.pack(
            fill="both",
            expand=True,
            pady=20
        )

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Productos registrados",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "stock"
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings"
        )

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("stock", text="Stock")

        tabla.column("codigo", width=100)
        tabla.column("nombre", width=180)
        tabla.column("precio", width=100)
        tabla.column("stock", width=100)

        for producto in self.restaurante_servicio.listar_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

        tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        columnas = ("usuario",)

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "usuario",
            width=250
        )

        for usuario in self.restaurante_servicio.listar_usuarios():
            tabla.insert(
                "",
                "end",
                values=(usuario.usuario,)
            )

        tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

    def ventas_pendientes(self):
        self.limpiar_contenido()

        mensaje = ttk.Label(
            self.contenido,
            text="La funcionalidad de Ventas está pendiente.",
            font=("Arial", 14)
        )
        mensaje.pack(pady=40)