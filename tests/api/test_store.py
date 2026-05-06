import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

ORDER_ID = 88776655

def test_consultar_inventario():
    response_get = requests.get(f"{BASE_URL}/store/inventory")
    assert response_get.status_code == 200
    assert isinstance(response_get.json(), dict)

def test_criar_e_consultar_pedido():
    payload_order = {
        "id": ORDER_ID,
        "petId": 987654321,
        "quantity": 1,
        "shipDate": "2024-05-10T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    
    response_post = requests.post(f"{BASE_URL}/store/order", json=payload_order, headers=HEADERS)
    assert response_post.status_code == 200
    assert response_post.json()["status"] == "placed"

    response_get = requests.get(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert response_get.status_code == 200
    assert response_get.json()["petId"] == 987654321

def test_deletar_pedido():
    response_delete = requests.delete(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert response_delete.status_code == 200