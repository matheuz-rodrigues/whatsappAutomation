import requests

def terminate_all_sessions():
    url = "https://whatsapp-api-8i0o.onrender.com/session/terminateAll"
    headers = {
        "accept": "application/json",
        "x-api-key": "6789",
    }
    response = requests.get(url, headers=headers)
    return print(response.json())
def start_session():
    url = f"https://whatsapp-api-8i0o.onrender.com/session/start/{input('Enter Session ID: ')}"
    headers = {
        "accept": "application/json",
        "x-api-key": "6789",
    }
    response = requests.get(url, headers=headers)
    return print(response.json())

def get_qr_image():
    session_name = input("Enter session name: ")
    url = f"https://whatsapp-api-8i0o.onrender.com/session/qr/{session_name}/image"
    headers = {
        "accept": "image/png",
        "x-api-key": "6789",
    }
    response = requests.get(url, headers=headers)

    # Verifica o tipo de conteúdo retornado
    content_type = response.headers.get("Content-Type", "")
    if "image/png" in content_type:
        return {"image": response.content}
    else:
        return {"json": response.json()}


result = get_qr_image()

if "image" in result:
    with open("qr_image.png", "wb") as file:
        file.write(result["image"])
    print("QR code salvo como 'qr_image.png'")
elif "json" in result:
    print("Resposta JSON:", result["json"])


def get_session_status():
    url = f"https://whatsapp-api-8i0o.onrender.com/session/status/{input("Digite o nome da sessão: ")}"
    headers = {
        "accept": "application/json",
        "x-api-key": "6789",
    }
    response = requests.get(url, headers=headers)
    return print(response.json())
