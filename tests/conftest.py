import pytest
from selenium import webdriver

@pytest.fixture()
def setup_teardown():
    options = webdriver.ChromeOptions()
    
    # 1. Configurações essenciais para rodar na Pipeline (GitHub Actions / Linux)
    #options.add_argument('--headless') # Roda o navegador em segundo plano (sem interface gráfica)
    options.add_argument('--no-sandbox') # Necessário para rodar no Ubuntu do GitHub Actions
    options.add_argument('--disable-dev-shm-usage') # Evita problemas de limite de memória no servidor
    options.add_argument('--window-size=1920,1080') # Garante o tamanho da tela para não esconder botões
    
    # 2. Inicializa o navegador com as opções configuradas
    driver = webdriver.Chrome(options=options)
    
    # 3. Configura uma espera implícita (espera até 5s para um elemento aparecer antes de dar erro)
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    # 4. Entrega o driver para o teste utilizar
    yield driver 
    
    # 5. Teardown: Fecha o navegador e encerra o processo após o fim do teste
    driver.quit()