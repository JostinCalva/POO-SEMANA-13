import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, restaurante_servicio, usuario):

        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.usuario = usuario

        self.root.title("Restaurante App - Semana 14")
        self.root.geometry("950x600")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        # ==========================================
        # CONTENEDOR PRINCIPAL
        # ==========================================

        self.frame_principal = ttk.Frame(
            self.root,
            padding=15
        )

        self.frame_principal.pack(
            fill="both",
            expand=True
        )

        # ==========================================
        # ENCABEZADO
        # ==========================================

        frame_encabezado = ttk.LabelFrame(
            self.frame_principal,
            text="Restaurante App",
            padding=10
        )

        frame_encabezado.pack(
            fill="x",
            pady=5
        )

        ttk.Label(
            frame_encabezado,
            text="Sistema de gestión",
            font=("Arial", 18, "bold")
        ).pack(side="left")

        ttk.Label(
            frame_encabezado,
            text="Usuario: " + self.usuario.nombre
        ).pack(side="right")

        # ==========================================
        # NAVEGACIÓN
        # ==========================================

        frame_navegacion = ttk.LabelFrame(
            self.frame_principal,
            text="Navegación",
            padding=10
        )

        frame_navegacion.pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            frame_navegacion,
            text="USUARIOS",
            command=self.mostrar_usuarios
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_navegacion,
            text="PRODUCTOS",
            command=self.mostrar_productos
        ).pack(
            side="left",
            padx=5
        )

        # ==========================================
        # CONTENIDO
        # ==========================================

        self.frame_contenido = ttk.Frame(
            self.frame_principal
        )

        self.frame_contenido.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.mostrar_productos()

    # ==============================================
    # LIMPIAR CONTENIDO
    # ==============================================

    def limpiar_contenido(self):

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    # ==============================================
    # USUARIOS
    # ==============================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        ttk.Label(
            self.frame_contenido,
            text="USUARIOS REGISTRADOS",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        frame_tabla = ttk.Frame(
            self.frame_contenido
        )

        frame_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "identificacion",
            width=200
        )

        tabla.column(
            "nombre",
            width=300
        )

        tabla.column(
            "usuario",
            width=200
        )

        tabla.pack(
            fill="both",
            expand=True
        )

        for usuario in self.restaurante_servicio.usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # ==============================================
    # PRODUCTOS
    # ==============================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        ttk.Label(
            self.frame_contenido,
            text="GESTIÓN DE PRODUCTOS",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        # ==========================================
        # FORMULARIO
        # ==========================================

        frame_formulario = ttk.LabelFrame(
            self.frame_contenido,
            text="Datos del producto",
            padding=10
        )

        frame_formulario.pack(
            fill="x",
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.entry_codigo = ttk.Entry(
            frame_formulario,
            width=25
        )

        self.entry_codigo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.entry_nombre = ttk.Entry(
            frame_formulario,
            width=25
        )

        self.entry_nombre.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Precio:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.entry_precio = ttk.Entry(
            frame_formulario,
            width=25
        )

        self.entry_precio.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Stock:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.entry_stock = ttk.Entry(
            frame_formulario,
            width=25
        )

        self.entry_stock.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # ==========================================
        # BOTONES
        # ==========================================

        frame_botones = ttk.Frame(
            self.frame_contenido
        )

        frame_botones.pack(
            fill="x",
            pady=10
        )

        ttk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Consultar / Cargar",
            command=self.cargar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=5
        )

        # ==========================================
        # TABLA
        # ==========================================

        frame_tabla = ttk.LabelFrame(
            self.frame_contenido,
            text="Productos registrados",
            padding=5
        )

        frame_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "codigo",
            width=150
        )

        self.tabla_productos.column(
            "nombre",
            width=280
        )

        self.tabla_productos.column(
            "precio",
            width=150
        )

        self.tabla_productos.column(
            "stock",
            width=150
        )

        self.tabla_productos.pack(
            fill="both",
            expand=True
        )

        self.actualizar_tabla()

    # ==============================================
    # REGISTRAR
    # ==============================================

    def registrar_producto(self):

        try:

            resultado = self.restaurante_servicio.registrar_producto(
                self.entry_codigo.get().strip(),
                self.entry_nombre.get().strip(),
                self.entry_precio.get().strip(),
                self.entry_stock.get().strip()
            )

            messagebox.showinfo(
                "Producto",
                resultado
            )

            self.limpiar_formulario()
            self.actualizar_tabla()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==============================================
    # CONSULTAR
    # ==============================================

    def cargar_producto(self):

        codigo = self.entry_codigo.get().strip()

        if not codigo:

            messagebox.showwarning(
                "Advertencia",
                "Ingrese el código del producto."
            )

            return

        producto = self.restaurante_servicio.buscar_producto(
            codigo
        )

        if producto is None:

            messagebox.showwarning(
                "Producto",
                "Producto no encontrado."
            )

            return

        self.entry_nombre.delete(0, tk.END)

        self.entry_nombre.insert(
            0,
            producto.nombre
        )

        self.entry_precio.delete(0, tk.END)

        self.entry_precio.insert(
            0,
            producto.precio
        )

        self.entry_stock.delete(0, tk.END)

        self.entry_stock.insert(
            0,
            producto.stock
        )

    # ==============================================
    # ACTUALIZAR
    # ==============================================

    def actualizar_producto(self):

        try:

            resultado = self.restaurante_servicio.actualizar_producto(
                self.entry_codigo.get().strip(),
                self.entry_nombre.get().strip(),
                self.entry_precio.get().strip(),
                self.entry_stock.get().strip()
            )

            messagebox.showinfo(
                "Producto",
                resultado
            )

            self.limpiar_formulario()
            self.actualizar_tabla()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==============================================
    # ELIMINAR
    # ==============================================

    def eliminar_producto(self):

        codigo = self.entry_codigo.get().strip()

        if not codigo:

            messagebox.showwarning(
                "Advertencia",
                "Ingrese el código del producto."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este producto?"
        )

        if not confirmar:
            return

        try:

            resultado = self.restaurante_servicio.eliminar_producto(
                codigo
            )

            messagebox.showinfo(
                "Producto",
                resultado
            )

            self.limpiar_formulario()
            self.actualizar_tabla()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==============================================
    # LIMPIAR
    # ==============================================

    def limpiar_formulario(self):

        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    # ==============================================
    # ACTUALIZAR TABLA
    # ==============================================

    def actualizar_tabla(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        for producto in self.restaurante_servicio.productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.precio,
                    producto.stock
                )
            )