import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QVBoxLayout, QPushButton

# Arrancamos con la ventana principal llamando al constructor de la clase base
class TiendaComponentesWindow(QWidget):
    def __init__(self):
        super().__init__()  
        
        # Le damos un título a la ventana para que el usuario sepa que es una tienda de componentes
        self.setWindowTitle("Tienda de Componentes de Computadora")

        # Creamos el layout vertical para organizar los widgets
        layout = QVBoxLayout()

        # Etiqueta inicial que guía al usuario sobre qué hacer: seleccionar un componente
        self.label = QLabel("Selecciona un componente de computadora:", self)
        layout.addWidget(self.label)  # La agregamos al layout

        # ComboBox para elegir un componente. Aquí damos las opciones para CPU, RAM, etc.
        self.combo_box = QComboBox(self)
        componentes_pc = ["CPU", "RAM", "Tarjeta Gráfica", "Disco Duro", "Placa Base"]  # Lista de componentes disponibles
        self.combo_box.addItems(componentes_pc)  # Añadimos los componentes a la lista desplegable
        layout.addWidget(self.combo_box)

        # SpinBox para seleccionar la cantidad de unidades del componente
        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(1, 6)  # Aquí se pueden elegir de 1 a 6 unidades
        self.spin_box.setSuffix(" unidades")  # Le agregamos un pequeño texto al número (ej. "2 unidades")
        layout.addWidget(self.spin_box)  # Lo añadimos al layout también

        # Botón para agregar el componente seleccionado y la cantidad al carrito
        self.boton = QPushButton("Agregar al Carrito", self)
        self.boton.clicked.connect(self.mostrar_seleccion)  # Conectamos el botón con la función que maneja la selección
        layout.addWidget(self.boton)

        # Finalmente, aplicamos el layout a la ventana
        self.setLayout(layout)

    # Esta función es la que se ejecuta cuando el botón es presionado
    def mostrar_seleccion(self):
        # Obtenemos el componente seleccionado en el ComboBox y la cantidad elegida en el SpinBox
        componente_seleccionado = self.combo_box.currentText()
        cantidad_seleccionada = self.spin_box.value()
        
        # Mostramos el resultado en la consola, simulando que el componente fue agregado al carrito
        print(f"Has agregado {cantidad_seleccionada} unidad(es) de {componente_seleccionado} al carrito.")

# creamos las variables para que funcione 
app = QApplication(sys.argv)
ventana = TiendaComponentesWindow()  # Creamos la ventana principal
ventana.show()  # Mostramos la ventana
sys.exit(app.exec_())  # Ejecutamos el loop de la aplicación hasta que el usuario la cierre
