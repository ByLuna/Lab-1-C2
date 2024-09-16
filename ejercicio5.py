import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class PersonaWindow(QWidget):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base

        # Le ponemos un título a la ventana que va a capturar los datos de una persona
        self.setWindowTitle("Datos de una Persona")
        
        # Creamos un layout vertical para apilar los widgets
        layout = QVBoxLayout()

        # Aquí tenemos una lista con características físicas y mentales que vamos a capturar
        caracteristicas_especificas = [
            "Altura (cm)", "Peso (kg)", "Color de cabello", "Color de ojos", "Tono de piel",  # Físicas
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración"  # Mentales
        ]

        # Lista donde vamos a guardar los campos de entrada (QLineEdit) para cada característica
        self.caracteristicas = []
        
        # Este loop recorre la lista de características y genera un campo de texto para cada una
        for i, caracteristica in enumerate(caracteristicas_especificas, start=1):
            # Creamos una etiqueta con el número y el nombre de la característica
            label = QLabel(f"{i}. {caracteristica}", self)
            layout.addWidget(label)

            # Creamos un campo de texto con un placeholder que indica qué debe ingresar el usuario
            campo = QLineEdit(self)
            campo.setPlaceholderText(f"Ingrese {caracteristica}")  # Esto es lo que aparece en gris dentro del campo
            layout.addWidget(campo)

            # Añadimos el campo de entrada a la lista para usarlo más tarde
            self.caracteristicas.append(campo)

        # Agregamos un botón que, al ser presionado, mostrará los datos ingresados
        self.boton = QPushButton("Mostrar Datos", self)
        self.boton.clicked.connect(self.mostrar_datos)  # Conectamos el botón a la función que muestra los datos
        layout.addWidget(self.boton)  # Añadimos el botón al layout

        # Finalmente, aplicamos el layout a la ventana
        self.setLayout(layout)

    # Función que muestra los datos ingresados en la consola
    def mostrar_datos(self):
        # Otra vez tenemos la lista de características, pero ahora solo con los nombres cortos
        caracteristicas_especificas = [
            "Altura", "Peso", "Color de cabello", "Color de ojos", "Tono de piel",
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración"
        ]

        # Recorremos cada campo de texto y mostramos lo que el usuario ingresó
        for idx, (campo, nombre) in enumerate(zip(self.caracteristicas, caracteristicas_especificas), start=1):
            # Imprimimos el nombre de la característica junto con el valor ingresado
            print(f"{nombre}: {campo.text()}")

# Código para iniciar el programa com PyQt5
app = QApplication(sys.argv)
ventana = PersonaWindow()  # Creamos la ventana principal
ventana.show()  # Mostramos la ventana
sys.exit(app.exec_())  # Ejecutamos el loop de eventos de la aplicación
