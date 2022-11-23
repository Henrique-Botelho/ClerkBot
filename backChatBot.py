from time import sleep
import pyautogui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# Configurações de tempo
timeLoadControl = 45
timeControl = 2


def sendMessage(message, contacts):
    # Download e definição do driver
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    sleep(10)
    navegador.get("https://web.whatsapp.com/")
    sleep(timeLoadControl)

    for contact in contacts:
        search = navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        sleep(timeControl)
        search.send_keys(contact)
        sleep(timeControl)
        pyautogui.press("Enter")
        sleep(timeControl)
        text = navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        sleep(timeControl)
        text.send_keys(message)
        sleep(timeControl)
        pyautogui.press("Enter")
        sleep(timeControl)
