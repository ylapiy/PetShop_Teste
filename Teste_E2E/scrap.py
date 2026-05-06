from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from Paginas import *

## o ideal seria passar a senha, o user a url e os dados pessoais para dentro de uma env
## MAS como todos essas dados são publico / exemplos apenas para o trabalho, acho isso
## desnecessario apenas faria que se alguem quisesse rodar isso localmente teria que setar a
## env por si mesma o que so adiciona trabalho desnecesario

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
    paginaPreencherCarinho(driver, wait)
    print("Itens adicionados e carrinho aberto.")
    paginaChekout(wait)
    paginaColocarDadosPessoais(wait)
    print("Adicionado dados pesoais de exemplo")
    paginaFinalizandoACompra(wait)
    print("Compra finalizada com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    driver.quit()
    print("tudo certo")
