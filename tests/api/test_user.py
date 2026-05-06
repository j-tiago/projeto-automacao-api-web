import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}
USERNAME = "automacao_qa_user"
USER_PAYLOAD = {
    "id": 10203040,
    "username": USERNAME,
    "firstName": "QA",
    "lastName": "Tester",
    "email": "qa@teste.com",
    "password": "senha_super_segura",
    "phone": "11999999999",
    "userStatus": 1
}

def test_criar_e_buscar_usuario():
    response_post = requests.post(f"{BASE_URL}/user", json=USER_PAYLOAD, headers=HEADERS)
    assert response_post.status_code == 200
    
    response_get = requests.get(f"{BASE_URL}/user/{USERNAME}")
    assert response_get.status_code == 200
    assert response_get.json()["firstName"] == "QA"

def test_login_usuario():
    params = {
        "username": USERNAME,
        "password": "senha_super_segura"
    }
    response_login = requests.get(f"{BASE_URL}/user/login", params=params)
    assert response_login.status_code == 200
    assert "logged in user session" in response_login.json()["message"]

def test_atualizar_e_deletar_usuario():
    payload_atualizado = USER_PAYLOAD.copy()
    payload_atualizado["firstName"] = "QA Atualizado"
    
    response_put = requests.put(f"{BASE_URL}/user/{USERNAME}", json=payload_atualizado, headers=HEADERS)
    assert response_put.status_code == 200
    
    response_delete = requests.delete(f"{BASE_URL}/user/{USERNAME}")
    assert response_delete.status_code == 200