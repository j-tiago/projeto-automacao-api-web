from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_fluxo_compra_e2e(setup_teardown):
    driver = setup_teardown
    wait = WebDriverWait(driver, 10) # Cria uma regra que pode esperar até 10s
    
    # 1. Login
    login_page = LoginPage(driver)
    login_page.fazer_login("standard_user", "secret_sauce")
    
    titulo_produtos = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_produtos == "Products"

    # 2. Adicionar produto ao carrinho
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # 3. Ir para o carrinho e clicar no checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    botao_checkout.click()
    
    # 4. A CORREÇÃO: Aguardar o campo 'first-name' ficar visível após a mudança de página
    campo_nome = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    campo_nome.send_keys("João Tiago")
    
    # Como o primeiro campo carregou, sabemos que o resto do formulário também já está na tela
    driver.find_element(By.ID, "last-name").send_keys("Desenvolvedor")
    driver.find_element(By.ID, "postal-code").send_keys("64000000")
    driver.find_element(By.ID, "continue").click()
    
    # 5. Finalizar compra
    botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    botao_finish.click()
    
    # 6. Asserção Final
    mensagem_sucesso = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert mensagem_sucesso == "Thank you for your order!"