import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        # Llamamos al constructor de la clase QWidget
        super().__init__()

        # Le damos un título a la ventana y un tamaño inicial
        self.setWindowTitle('Ingresar Cédula y Nombre')
        self.setGeometry(100, 100, 300, 250)

        # Etiquetas que guiarán al usuario a ingresar su cédula y nombre
        self.cedula_label = QLabel('Número de Cédula:', self)
        self.nombre_label = QLabel('Nombre Completo:', self)

        # Etiqueta para mostrar el resultado (centrada)
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)

        # Campos de entrada para la cédula y el nombre, con pequeños recordatorios (placeholders)
        self.cedula_input = QLineEdit(self)
        self.cedula_input.setPlaceholderText("Número de cédula")
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Nombre completo")

        # Botón que, al ser presionado, mostrará los datos ingresados
        self.boton_mostrar = QPushButton('Mostrar Datos', self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)  # Cuando se presiona, llamamos a mostrar_datos

        # Organizamos todo con un layout vertical para que los elementos se apilen
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)

        # Aplicamos el layout a la ventana
        self.setLayout(layout)

    # Función que muestra los datos cuando presionamos el botón
    def mostrar_datos(self):
        # Obtenemos lo que el usuario ha escrito en los campos
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        # Si ambos campos tienen texto, mostramos los datos; si no, pedimos al usuario que complete ambos
        if cedula and nombre:
            self.resultado_label.setText(f'Cédula: {cedula}\nNombre: {nombre}')
        else:
            self.resultado_label.setText('Por favor, ingresa ambos datos.')

# Código que inicia la app y muestra la ventana
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Creamos la aplicación
    ventana = VentanaPrincipal()   # Creamos la ventana principal
    ventana.show()                 # Mostramos la ventana
    sys.exit(app.exec_())          # Ejecutamos la app hasta que el usuario cierre la ventana
