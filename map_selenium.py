from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



def get_screenshot_street_view(address):
    user_dir = 'C:/tmp/selenium'
    
    # Configuração do WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument(f"user-data-dir={user_dir}")
    url = 'https://www.google.com.br/maps/preview'
    # Inicialização do WebDriver
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    # Localizar o campo de entrada pelo nome, ID, XPath ou outros métodos
    search_text_input = driver.find_element(By.XPATH, """//*[@id="searchboxinput"]""")
    # Inserir texto no campo
    search_text_input.send_keys(address)

    search = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="searchbox-searchbutton"]""")))
    search.click()
    view_map = wait.until(EC.presence_of_element_located((By.XPATH,  """//*[@id="runway-expand-button"]/div/button/div/div""")))
    view_map.click()
    sleep(2)
    collapse_panel = driver.find_element(By.XPATH, """//*[@id="QA0Szd"]/div/div/div[2]/button""")
    collapse_panel.click()
    sleep(2)
    # Tirar um print da tela e salvar a imagem localmente
    driver.save_screenshot('screenshot.png')
    sleep(2)
    driver.quit()


# Farmácia Pague Menos
get_screenshot_street_view("Av. Presidente Wilson, 706 - Centro, São Vicente - SP, 11320-000")


