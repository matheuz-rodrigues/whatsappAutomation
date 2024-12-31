import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visualizador de Imagens")
        self.setGeometry(100, 100, 300, 300)

        # Layout principal
        self.layout = QVBoxLayout()

        # Label para exibir a imagem
        self.image_label = QLabel()
        self.image_label.setStyleSheet("border: 1px solid black;")
        self.image_label.setScaledContents(True)

        # Adicionar widgets ao layout
        self.layout.addWidget(self.image_label)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Exibir a imagem padrão ao iniciar
        self.show_default_image()

    def show_default_image(self):
        # Caminho para a imagem padrão nos arquivos do projeto
        image_path = "qr_image.png"  # Altere para o caminho correto no seu projeto
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():  # Verifica se a imagem foi carregada com sucesso
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("Imagem padrão não encontrada")
            self.image_label.setStyleSheet("color: red; font-size: 16px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())

'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 400, 300)

        # Layout e botão
        layout = QVBoxLayout()
        button = QPushButton("Ir para o QR Code")
        button.clicked.connect(self.open_qr_code_window)
        layout.addWidget(button)

        # Configurar widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_qr_code_window(self):
        self.qr_code_window = QRCodeWindow()
        self.qr_code_window.show()
        self.close()  # Fecha a janela de login

class QRCodeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de QR Code")
        self.setGeometry(150, 150, 400, 300)

        # Layout e botão
        layout = QVBoxLayout()
        button = QPushButton("Voltar para o Login")
        button.clicked.connect(self.open_login_window)
        layout.addWidget(button)

        # Configurar widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()  # Fecha a janela de QR Code

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
'''