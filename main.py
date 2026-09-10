import os
import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):
        self.root = root

        self.root.title("Restaurante App")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        carpeta_datos = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "datos"
        )

        archivo_servicio = ArchivoServicio(carpeta_datos)

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()

        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_login
        )


def main():
    root = tk.Tk()

    app = RestauranteApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()