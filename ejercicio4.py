import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MascotasWindow(QWidget):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base
        
        # Le ponemos un título a la ventana, algo básico pero necesario
        self.setWindowTitle("Datos de Mascotas")

        # Creamos el layout vertical para colocar los elementos de forma apilada
        layout = QVBoxLayout()

        # Lista para almacenar las entradas (nombre, especie, edad) de cada mascota
        self.mascotas = []
        
        # Vamos a crear campos para 3 mascotas, repitiendo el proceso para cada una
        for i in range(1, 4):
            # Mostramos la etiqueta para cada mascota (Mascota 1, Mascota 2, etc.)
            layout.addWidget(QLabel(f"Mascota {i}"))

            # Creamos un campo de texto para el nombre de la mascota y lo agregamos al layout
            nombre = QLineEdit(self)
            nombre.setPlaceholderText(f"Nombre de la mascota {i}")  # Este es el texto guía que aparece en el campo
            layout.addWidget(nombre)

            # Campo de texto para la especie de la mascota (perro, gato, etc.)
            especie = QLineEdit(self)
            especie.setPlaceholderText(f"Especie de la mascota {i}")  # Otro recordatorio para el usuario
            layout.addWidget(especie)

            # Campo de texto para la edad de la mascota
            edad = QLineEdit(self)
            edad.setPlaceholderText(f"Edad de la mascota {i}")  # Este placeholder explica qué ingresar aquí
            layout.addWidget(edad)

            # Guardamos los tres campos (nombre, especie, edad) en una tupla y lo añadimos a la lista de mascotas
            self.mascotas.append((nombre, especie, edad))

        # Botón para mostrar los datos ingresados cuando lo presionas
        self.boton = QPushButton("Mostrar Datos", self)
        # Conectamos el botón con la función que se encarga de mostrar los datos
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)  # Lo añadimos al layout

        # Establecemos el layout de la ventana
        self.setLayout(layout)

    # Esta función se encarga de imprimir los datos de cada mascota
    def mostrar_datos(self):
        # Recorremos la lista de mascotas, que tiene los campos de cada una
        for idx, (nombre, especie, edad) in enumerate(self.mascotas, start=1):
            # Imprimimos la info de cada mascota, índice incluido para numerarlas
            print(f"Mascota {idx}:")
            print(f"Nombre: {nombre.text()}")  # Obtenemos el texto que el usuario ingresó
            print(f"Especie: {especie.text()}")  # Lo mismo para la especie
            print(f"Edad: {edad.text()}")  # Y para la edad
            print("---")  # Un separador para mayor claridad

# Creamos la aplicación y la ventana
app = QApplication(sys.argv)
ventana = MascotasWindow()
ventana.show()  # Mostramos la ventana
sys.exit(app.exec_())  # Ejecutamos el loop de la aplicación hasta que el usuario la cierre
