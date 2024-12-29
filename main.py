import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from telaLogin import Ui_Form  # Importando o código gerado

#cria a sessão
'''api_key = input("Enter your API key: ")
sessao_id = input('Digite o seu sessao id: ')

def criar_sessao():
    # URL da API
    url = f"http://localhost:3000/session/start/{sessao_id}"
    headers = {
        "accept": "application/json",
        "x-api-key": f"{api_key}"
    }

    response = requests.get(url, headers=headers)
    print(response.json())

def sessao_status():
    # URL da API
    url = f"http://localhost:3000/session/status/{sessao_id}"

    # Cabeçalhos
    headers = {
        "accept": "application/json",
        "x-api-key": f"{api_key}"
    }

    # Realizando a requisição GET
    response = requests.get(url, headers=headers)

    # Exibindo a resposta
    if response.status_code == 200:
        print("Status Code:", response.status_code)
        print("Response Body:", response.json())
    else:
        print("Erro ao obter o status. Status code:", response.status_code)
        print("Detalhes:", response.text)

def terminar_tudo():

    url = f"http://localhost:3000/session/terminateAll"
    headers = { "x-api-key": f"{api_key}"}
    response = requests.get(url, headers=headers)
    print(response.json())

'''


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
            #puxa a outra a tela do qr code
            pass
        elif api_key != "6789" and session_id == "dig":
            self.status.setText("Id da sessão Incorreto")
        elif api_key == "6789" and session_id != "producao":
            self.status.setText("Chave Incorreta")
        else: self.status.setText("Dados Inválidos")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaLogin()
    janela.show()
    sys.exit(app.exec_())
