from time import sleep

import requests
import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5.QtGui import QKeySequence, QPixmap
from telaLogin import Ui_Form
from qrCodeViewer import Ui_qrCodeViewer
session_id ="t"
class TelaLogin(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnEntrar.clicked.connect(self.entrar)
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.btnEntrar.click)

    def entrar(self):
        api_key = self.inputApiKey.text()
        session_id = self.inputId.text()

        if api_key == "6789" and session_id == "dig":

            # URL e cabeçalhos para a requisição
            url = f"https://whatsapp-api-8i0o.onrender.com/session/qr/{session_id}/image"
            headers = {
                "accept": "image/png",
                "x-api-key": "6789",
            }

            # Fazendo a requisição
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Levanta uma exceção em caso de erro na requisição
            except requests.exceptions.RequestException as e:
                print(f"Erro na requisição: {e}")
                self.status.setText("Erro na requisição. Tente novamente.")
                return

            # Verifica o tipo de conteúdo retornado
            content_type = response.headers.get("Content-Type", "")
            if "image/png" in content_type:
                # Salva a imagem
                with open("qr_image.png", "wb") as file:
                    file.write(response.content)
                print("QR code salvo como 'qr_image.png'")

                # Depois de obter a imagem, abre a tela do QR Code
                try:
                    self.qr_code_window = QRCodeViewer()  # Tente criar a janela
                    self.qr_code_window.show()  # Tente exibir a janela
                    self.close()  # Fecha a janela de login
                except Exception as e:
                    print(f"Erro ao abrir a janela do QR Code: {e}")
                    self.status.setText("Erro ao abrir a janela do QR Code.")
            elif "application/json" in content_type:
                # Exibe o JSON
                print("Resposta JSON:", response.json())
            else:
                print("Tipo de conteúdo desconhecido:", content_type)
                self.status.setText("Tipo de conteúdo inesperado.")

        elif api_key != "6789" and session_id == "dig":
            self.status.setText("Id da sessão Incorreto")
        elif api_key == "6789" and session_id != "dig":
            self.status.setText("Chave Incorreta")
        else:
            self.status.setText("Dados Inválidos")


class QRCodeViewer(QWidget, Ui_qrCodeViewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a interface gerada pelo Qt Designer
        self.exibir_qr_code()  # Exibe a imagem do QR Code logo após a inicialização
        self.verificar_conexao()

    def exibir_qr_code(self):
        try:
            # Carrega a imagem salva
            pixmap = QPixmap("qr_image.png")
            if pixmap.isNull():  # Verifica se a imagem foi carregada corretamente
                print("Falha ao carregar a imagem.")
                self.status.setText("Falha ao carregar a imagem.")
                return

            # Exibe a imagem no QLabel 'qr'
            self.qr.setPixmap(pixmap)
            self.qr.setScaledContents(True)  # Ajusta a imagem para o tamanho do QLabel
        except Exception as e:
            print(f"Erro ao exibir a imagem: {e}")
            self.status.setText("Erro ao exibir a imagem.")



    def verificar_conexao(self):
        print(session_id)
        try:
            url = f"https://whatsapp-api-8i0o.onrender.com/session/status/{session_id}"
            headers = {
                "accept": "application/json",
                "x-api-key": "6789",
            }
            response = requests.get(url, headers=headers)
            print(session_id)
            return print(response.json())
        except: print(session_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaLogin()
    janela.show()
    sys.exit(app.exec_())
