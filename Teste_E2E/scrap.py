from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

from Paginas import (
    paginaLogin,
    preencherCarinho,
    colocarDadosPessoais,
    finalizandoACompra,
)

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com")
    paginaLogin(wait)
    print("Login realizado.")
    preencherCarinho(driver, wait)
    print("Itens adicionados e carrinho aberto.")
    colocarDadosPessoais(wait)
    finalizandoACompra(wait)
    print("Compra finalizada com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    driver.quit()
    print("tudo certo")
