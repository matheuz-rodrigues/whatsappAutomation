import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QShortcut
from PyQt5.QtGui import QKeySequence


# Atalho para o botão




class MainWindow(QMainWindow):
    def __init__(self):


        super().__init__()

        self.setWindowTitle("Exemplo - Enter ativa botão")
        self.setGeometry(200, 200, 300, 200)

        # Campo de texto
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Digite algo e pressione Enter...")

        # Botão
        self.button = QPushButton("Clique-me")
        self.button.clicked.connect(self.button_clicked)

        # Configurar botão como padrão
        self.button.setDefault(True)



        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_clicked(self):
        print(f"Texto digitado: {self.input_field.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
