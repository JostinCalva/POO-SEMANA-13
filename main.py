import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):

        self.root = root

        archivo_servicio = ArchivoServicio()

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        self.mostrar_login()

    def mostrar_login(self):

        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self, usuario):

        for widget in self.root.winfo_children():
            widget.destroy()

        MainView(
            self.root,
            self.restaurante_servicio,
            usuario
        )


def main():

    root = tk.Tk()

    RestauranteApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()