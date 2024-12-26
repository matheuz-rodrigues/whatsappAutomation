import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget
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
        self.setupUi(self)  # Configura a interface
        # Adicionar funcionalidades, como conectar o botão a um método
        self.pushButton.clicked.connect(self.entrar)

    def entrar(self):
        chave = self.lineEdit.text()  # Obtendo o texto do campo 'chave'
        sessao = self.lineEdit_2.text()  # Obtendo o texto do campo 'ID da Sessão'

        # Aqui você pode adicionar o código para validar os dados
        print(f"Chave: {chave}, Sessão: {sessao}")

        # Por exemplo, você pode verificar se a chave está vazia e mostrar um erro
        if not chave or not sessao:
            print("Por favor, preencha todos os campos.")
        else:
            print("Dados validados com sucesso!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaLogin()
    janela.show()
    sys.exit(app.exec_())
