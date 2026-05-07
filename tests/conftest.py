import pytest
from selenium import webdriver

@pytest.fixture()
def setup_teardown():
    options = webdriver.ChromeOptions()
    
    # --- O Segredo para CI/CD no GitHub Actions ---
    # Usa o novo motor headless do Chrome, idêntico a um monitor real
    options.add_argument('--headless=new') 
    
    options.add_argument('--no-sandbox') 
    options.add_argument('--disable-dev-shm-usage') 
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu') # Dá mais estabilidade no Ubuntu
    
    # Disfarça o robô simulando um usuário real no Windows
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    yield driver 
    
    driver.quit()