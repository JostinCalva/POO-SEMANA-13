# Restaurante App - Semana 14
## Nombre Jostin Calva
## Descripción

Proyecto desarrollado para la Semana 14 de la asignatura Programación Orientada a Objetos.

En esta semana se evolucionó la aplicación gráfica del restaurante mediante el uso de componentes, contenedores y gestores de geometría de Tkinter y ttk.

La aplicación permite iniciar sesión, consultar usuarios y gestionar productos mediante una interfaz gráfica organizada.

## Objetivo

Aplicar los fundamentos de componentes y contenedores en Tkinter, manteniendo la arquitectura modular del proyecto y la separación de responsabilidades entre modelos, servicios, interfaz y datos.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Componentes utilizados

La interfaz gráfica utiliza componentes de Tkinter y ttk, entre ellos:

* `Tk`
* `Frame`
* `LabelFrame`
* `Label`
* `Entry`
* `Button`
* `Treeview`
* `messagebox`

Esto
