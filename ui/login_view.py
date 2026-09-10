import tkinter as tk
from tkinter import ttk


class LoginView:

    def __init__(self, root, restaurante_servicio, mostrar_principal):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_principal = mostrar_principal

        self.frame = ttk.Frame(self.root, padding=30)
        self.frame.pack(fill="both", expand=True)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=(30, 10))

        subtitulo = ttk.Label(
            self.frame,
            text="Inicio de sesión"
        )
        subtitulo.pack(pady=(0, 20))

        ttk.Label(
            self.frame,
            text="Usuario:"
        ).pack(pady=(10, 5))

        self.usuario_entry = ttk.Entry(
            self.frame,
            width=30
        )
        self.usuario_entry.pack()

        ttk.Label(
            self.frame,
            text="Contraseña:"
        ).pack(pady=(10, 5))

        self.contrasena_entry = ttk.Entry(
            self.frame,
            width=30,
            show="*"
        )
        self.contrasena_entry.pack()

        self.mensaje = ttk.Label(
            self.frame,
            text=""
        )
        self.mensaje.pack(pady=15)

        boton_ingresar = ttk.Button(
            self.frame,
            text="Ingresar",
            command=self.ingresar
        )
        boton_ingresar.pack(pady=10)

        self.usuario_entry.focus()

    def ingresar(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje.config(
                text="Complete todos los campos."
            )
            return

        acceso_correcto = self.restaurante_servicio.validar_acceso(
            usuario,
            contrasena
        )

        if acceso_correcto:
            self.frame.destroy()
            self.mostrar_principal()
        else:
            self.mensaje.config(
                text="Usuario o contraseña incorrectos."
            )