import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

# Creamos la clase de la ventana principal
class VentanaPrincipal(QWidget):
    def __init__(self):
        # Llamamos al constructor de la clase base (QWidget)
        super().__init__()

        # Establecemos el título de la ventana y sus dimensiones
        self.setWindowTitle('Ingresar Clave Secreta')
        self.setGeometry(100, 100, 300, 200)

        # Creamos una etiqueta con las instrucciones y centramos el texto
        self.instrucciones_label = QLabel('Ingresa tu clave secreta:', self)
        self.instrucciones_label.setAlignment(Qt.AlignCenter)

        # Creamos un campo de entrada para la clave secreta y configuramos para que muestre los caracteres como asteriscos
        self.clave_input = QLineEdit(self)
        self.clave_input.setEchoMode(QLineEdit.Password)  # Esto oculta la clave con asteriscos
        self.clave_input.setPlaceholderText("Clave secreta")  # Texto que aparece como guía en el campo

        # Botón para mostrar la clave ingresada
        self.boton_mostrar = QPushButton('Mostrar Clave', self)
        # Conectamos el clic del botón con la función que mostrará la clave
        self.boton_mostrar.clicked.connect(self.mostrar_clave)

        # Etiqueta para mostrar la clave que el usuario ingresó (inicialmente vacía)
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)  # Centramos el texto en la etiqueta

        # Creamos el layout (organización visual) y añadimos los widgets (elementos de la ventana)
        layout = QVBoxLayout()
        layout.addWidget(self.instrucciones_label)  # Añadimos las instrucciones
        layout.addWidget(self.clave_input)          # Añadimos el campo de entrada para la clave
        layout.addWidget(self.boton_mostrar)        # Añadimos el botón de mostrar clave
        layout.addWidget(self.resultado_label)      # Añadimos la etiqueta del resultado

        # Establecemos el layout para que sea el diseño principal de la ventana
        self.setLayout(layout)

    # Función que se ejecuta cuando se presiona el botón "Mostrar Clave"
    def mostrar_clave(self):
        # Obtenemos el texto (clave secreta) que el usuario ingresó en el campo de entrada
        clave = self.clave_input.text()
        # Mostramos la clave ingresada en la etiqueta de resultado
        self.resultado_label.setText(f'Clave ingresada: {clave}')

# Este bloque se asegura de que la aplicación funcione correctamente
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Iniciamos la aplicación
    ventana = VentanaPrincipal()   # Creamos la ventana principal
    ventana.show()                 # Mostramos la ventana
    sys.exit(app.exec_())          # Ejecutamos el loop de la aplicación
