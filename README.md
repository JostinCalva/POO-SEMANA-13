# Restaurante App - Semana 13

# Jostin Anthony Calva Salinas

Aplicación desarrollada para la asignatura Programación Orientada a Objetos, correspondiente a la Semana 13.

En esta etapa se inicia la transición de la aplicación de consola hacia una interfaz gráfica de usuario utilizando Tkinter.

## Objetivo

Implementar una estructura gráfica básica para el sistema Restaurante App, utilizando modelos, servicios, archivos JSON y vistas independientes.

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