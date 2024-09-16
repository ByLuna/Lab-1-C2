import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QFormLayout

# Creamos la clase de la ventana principal
class VentanaPrincipal(QWidget):
    def __init__(self):
        # Llamamos al constructor de la clase base (QWidget)
        super().__init__()

        # Definimos el título de la ventana y su tamaño
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)

        # Creamos etiquetas para el nombre y la edad
        self.nombre_label = QLabel('Nombre Completo:', self)
        self.edad_label = QLabel('Edad:', self)

        # Creamos campos de entrada donde el usuario escribe el nombre y la edad
        self.nombre_input = QLineEdit(self)
        self.edad_input = QLineEdit(self)

        # Aqui se mostrará el resultado cuando se actualicen los datos
        self.resultado_label = QLabel('', self)

        # Este Botón funciona para actualizar los datos ingresados
        self.boton_actualizar = QPushButton('Actualizar', self)
        # Conectamos el botón con la función que actualizará la información
        self.boton_actualizar.clicked.connect(self.actualizar_datos)

        # Usamos un layout para organizar los elementos visuales de la ventana
        layout = QFormLayout()
        layout.addRow(self.nombre_label, self.nombre_input)  # Añadimos el de nombre y su campo de entrada
        layout.addRow(self.edad_label, self.edad_input)      # Añadimos la edad y su campo de entrada
        layout.addRow(self.boton_actualizar, self.resultado_label)  # Añadimos el botón y el espacio para el resultado

        # Aplicamos el layout a la ventana
        self.setLayout(layout)

    # Esta función se ejecutara cuando se presiona el botón
    def actualizar_datos(self):
        # Obtenemos el texto que el usuario escribió en los campos de nombre y edad
        nombre = self.nombre_input.text()
        edad = self.edad_input.text()
        # Actualizamos para mostrar el nombre y la edad ingresados
        self.resultado_label.setText(f'Nombre Completo: {nombre}\nEdad: {edad}')

# Este bloque se asegura de que la aplicación se ejecute correctamente
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Iniciamos la aplicación
    ventana = VentanaPrincipal()   # Creamos la ventana principal
    ventana.show()                 # Mostramos la ventana
    sys.exit(app.exec_())          # Ejecutamos el loop de la aplicación
