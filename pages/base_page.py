class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def encontrar_elemento(self, localizador):
        return self.driver.find_element(*localizador)

    def escrever(self, localizador, texto):
        self.encontrar_elemento(localizador).send_keys(texto)

    def clicar(self, localizador):
        self.encontrar_elemento(localizador).click()