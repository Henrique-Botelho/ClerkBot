from time import sleep
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# Configurações de tempo
timeLoadControl = 35
timeControl = 1.5


def sendMessage(message, contacts, images, documents):
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
        if len(images) > 0:
            for image in images:
                clip = navegador.find_element(By.CSS_SELECTOR,  'span[data-icon="clip"]')
                clip.click()
                sleep(timeControl)
                clipMidia = navegador.find_element(By.CSS_SELECTOR, 'input[type=file]')
                sleep(timeControl)
                clipMidia.send_keys(image)
                sleep(timeControl)
                send = navegador.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
                send.click()
                sleep(timeControl)

        if len(documents) > 0:
            for document in documents:
                clip = navegador.find_element(By.CSS_SELECTOR,  'span[data-icon="clip"]')
                clip.click()
                sleep(timeControl)
                clipDocs = navegador.find_element(By.CSS_SELECTOR, 'input[type=file]')
                clipDocs.send_keys(document)
                sleep(timeControl)
                send = navegador.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
                send.click()
                sleep(timeControl)

