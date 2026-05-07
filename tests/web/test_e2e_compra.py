from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_fluxo_compra_e2e(setup_teardown):
    driver = setup_teardown
    wait = WebDriverWait(driver, 10) 
    
    try:
        # 1. Login
        login_page = LoginPage(driver)
        login_page.fazer_login("standard_user", "secret_sauce")
        
        # 2. Esperar o título da página de produtos aparecer
        titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
        assert titulo == "Products"

        # 3. Adicionar produto
        botao_add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        botao_add.click()
        
        # 4. Ir para o carrinho (A MÁGICA ACONTECE AQUI - Clique via JavaScript)
        carrinho = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
        driver.execute_script("arguments[0].click();", carrinho)
        
        # 5. Ir para o Checkout
        botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        botao_checkout.click()
        
        # 6. Preencher formulário
        campo_nome = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        campo_nome.send_keys("João Tiago")
        driver.find_element(By.ID, "last-name").send_keys("Desenvolvedor")
        driver.find_element(By.ID, "postal-code").send_keys("64000000")
        
        botao_continue = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        botao_continue.click()
        
        # 7. Finalizar compra
        botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        botao_finish.click()
        
        # 8. Asserção Final
        mensagem_sucesso = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
        assert mensagem_sucesso == "Thank you for your order!"
        
    except Exception as erro:
        driver.save_screenshot("erro_tela.png")
        raise erro