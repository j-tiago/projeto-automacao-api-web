import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

def test_adicionar_e_consultar_pet():
    payload_pet = {
        "id": 987654321,
        "category": {"id": 1, "name": "Cachorro"},
        "name": "Rex",
        "photoUrls": ["string"],
        "tags": [{"id": 1, "name": "Dócil"}],
        "status": "available"
    }
    
    response_post = requests.post(f"{BASE_URL}/pet", json=payload_pet, headers=HEADERS)
    assert response_post.status_code == 200
    assert response_post.json()["name"] == "Rex"

    response_get = requests.get(f"{BASE_URL}/pet/987654321")
    assert response_get.status_code == 200
    assert response_get.json()["status"] == "available"

def test_atualizar_status_pet():
    payload_atualizado = {
        "id": 987654321,
        "name": "Rex",
        "status": "sold"
    }
    
    response_put = requests.put(f"{BASE_URL}/pet", json=payload_atualizado, headers=HEADERS)
    assert response_put.status_code == 200
    assert response_put.json()["status"] == "sold"