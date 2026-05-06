from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_fluxo_compra_e2e(setup_teardown):
    driver = setup_teardown
    
    login_page = LoginPage(driver)
    login_page.fazer_login("standard_user", "secret_sauce")
    
    titulo_produtos = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_produtos == "Products"

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("João Tiago")
    driver.find_element(By.ID, "last-name").send_keys("Desenvolvedor")
    driver.find_element(By.ID, "postal-code").send_keys("64000000")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    
    mensagem_sucesso = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensagem_sucesso == "Thank you for your order!"