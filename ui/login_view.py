import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(self, root, restaurante_servicio, abrir_principal):

        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.abrir_principal = abrir_principal

        self.root.title("Restaurante App - Inicio de Sesión")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # CONTENEDOR PRINCIPAL
        frame_principal = ttk.Frame(
            self.root,
            padding=30
        )
        frame_principal.pack(
            fill="both",
            expand=True
        )

        # TITULO
        ttk.Label(
            frame_principal,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        ).pack(pady=(10, 5))

        ttk.Label(
            frame_principal,
            text="Inicio de sesión",
            font=("Arial", 14)
        ).pack(pady=(0, 20))

        # FORMULARIO
        frame_formulario = ttk.LabelFrame(
            frame_principal,
            text="Datos de acceso",
            padding=20
        )
        frame_formulario.pack(
            fill="x",
            padx=20
        )

        # USUARIO
        ttk.Label(
            frame_formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_usuario = ttk.Entry(
            frame_formulario,
            width=30
        )
        self.entry_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # CONTRASEÑA
        ttk.Label(
            frame_formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_password = ttk.Entry(
            frame_formulario,
            width=30,
            show="*"
        )
        self.entry_password.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # BOTON INGRESAR
        frame_boton = ttk.Frame(
            frame_principal
        )
        frame_boton.pack(
            pady=25
        )

        ttk.Button(
            frame_boton,
            text="INGRESAR",
            command=self.ingresar
        ).pack(
            ipadx=20,
            ipady=5
        )

        # DATOS DE PRUEBA
        ttk.Label(
            frame_principal,
            text="Usuario de prueba: admin  |  Contraseña: 1234"
        ).pack(
            pady=5
        )

    def ingresar(self):

        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning(
                "Advertencia",
                "Ingrese el usuario y la contraseña."
            )
            return

        acceso_correcto = self.restaurante_servicio.validar_acceso(
            usuario,
            password
        )

        if acceso_correcto is None:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.abrir_principal(
            acceso_correcto
        )