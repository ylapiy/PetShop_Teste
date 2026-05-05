from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def paginaLogin(wait):
    EntradasLogin = {
        "login": {"by": (By.ID, "user-name"), "valor": "standard_user"},
        "senha": {"by": (By.ID, "password"), "valor": "secret_sauce"},
    }
    for chave, dados in EntradasLogin.items():
        elemento = wait.until(EC.element_to_be_clickable(dados["by"]))
        elemento.clear()
        elemento.send_keys(dados["valor"])

    botao_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    botao_login.click()


def preencherCarinho(driver, wait):

    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
    botoes = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    for botao in botoes:
        try:
            driver.execute_script("arguments[0].click();", botao)
        except Exception as e:
            print(f"Erro ao clicar em um dos botões: {e}")

    carrinho = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    carrinho.click()
    btn_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    btn_checkout.click()


def colocarDadosPessoais(wait):
    EntradasPesoais = {
        "nomeF": {"by": (By.ID, "first-name"), "valor": "Ygor"},
        "nomeL": {"by": (By.ID, "last-name"), "valor": "Félix"},
        "Zip": {"by": (By.ID, "postal-code"), "valor": "M5V 3L9"},
    }
    for chave, dados in EntradasPesoais.items():
        elemento = wait.until(EC.element_to_be_clickable(dados["by"]))
        elemento.clear()
        elemento.send_keys(dados["valor"])


def finalizandoACompra(wait):
    btn_continue = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    btn_continue.click()
    btn_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    btn_finish.click()
