from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_LOGIN = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        self.driver.get("https://www.saucedemo.com/")
        self.escrever(self.CAMPO_USUARIO, usuario)
        self.escrever(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_LOGIN)