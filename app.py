from flask import Flask
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


app = Flask(__name__)

# @app.route('/')
# def login_travian():


#
#     options = Options()
#
#     # Set some options to make the browser more stealthy
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('--disable-extensions')
#     options.add_argument('--disable-infobars')
#     options.add_argument('--disable-popup-blocking')
#     options.add_argument('--disable-notifications')
#     options.add_argument('--disable-default-apps')
#     options.add_argument('--disable-extensions-file-access-check')
#     options.add_argument('--disable-web-security')
#     options.add_argument('--disable-logging')
#     options.add_argument('--disable-translate')
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--start-maximized')
#     options.add_argument('--incognito')
#
#     # Set the user agent to make it look more like a real browser
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
#
#     # Set up the WebDriver
#     driver = webdriver.Chrome(options=options)
#
#     # Navigate to the login page
#     driver.get('https://ts8.x1.europe.travian.com/login.php')
#
#     # Wait for the login form to appear
#     wait = WebDriverWait(driver, 5)
#     form = wait.until(EC.presence_of_element_located((By.ID, 'loginForm')))
#
#     print(form)
#
#     # Fill in the login form
#     username_field = form.find_element("name", "name")
#     password_field = form.find_element("name", "password")
#     username_field.send_keys('enzysss123')
#     password_field.send_keys('lol123')
#     login_button = form.find_element("xpath", "//button[@type='submit']")
#     login_button.click()
#
#     # Wait for the login to complete
#     wait.until(EC.url_changes(driver.current_url))
#     cookies = driver.get_cookies()
#     #print(cookies)
#     # Close the WebDriver
#     cookiess = {cookie["name"]: cookie["value"] for cookie in driver.get_cookies()}
#     driver.close()
#     #ampliaCampi(cookies)
#
#     # Richiede la pagina del campo da potenziare
#     session = requests.Session()
#     for cookie in cookies:
#         session.cookies.set(cookie['name'], cookie['value'])
#     url = "https://ts8.x1.europe.travian.com/karte.php?x=134&y=-66"
#     payload = {
#
#         "id": 16,  # ID del campo da potenziare
#         "gid": 2,  # GID del tipo di campo (in questo caso, il GID dell'edificio principale)
#     }
#
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#
# # Invio della richiesta POST per potenziare il campo
#
#     response = session.post(url, headers=headers)
#     return (response.text)
#
#
#     if response.status_code == 200:
#         print("Campo potenziato con successo!")
#     else:
#         print("Errore durante il potenziamento del campo.")




@app.route('/')
def loginProxy():
    try:
        # Imposta il percorso dell'eseguibile del browser Chrome
        chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"

        # Crea un'istanza dell'oggetto ChromeOptions per configurare il browser
        chrome_options = webdriver.ChromeOptions()

        # Imposta il percorso della cartella dei dati del browser
        chrome_options.add_argument("--user-data-dir=/opt/render/project/.render/chrome/data")

        # Crea un'istanza dell'oggetto webdriver di Chrome
        driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)

        print('dopo driver')

        # codice per eseguire il login
        driver.get('https://ts9.x1.europe.travian.com/login.php')
        
        # Wait for the login form to appear
        wait = WebDriverWait(driver, 10)
        form = wait.until(EC.presence_of_element_located((By.ID, 'loginForm')))
        # Fill in the login form
        username_field = form.find_element("name", "name")
        password_field = form.find_element("name", "password")
        username_field.send_keys('gigio4422')
        password_field.send_keys('lol123')
        login_button = form.find_element("xpath", "//button[@type='submit']")
        login_button.click()
        # Wait for the login to complete
        wait.until(EC.url_changes(driver.current_url))
    except WebDriverException as e:
        # gestione dell'eccezione
        print(f"Errore durante l'esecuzione del webdriver: {e}")
        driver.quit()
        # eventuali altre operazioni per gestire l'errore
        return 'Login effettuato con successo'
    # Definizione dell'User-Agent
    #user_agent = UserAgent().random
    # Definizione delle opzioni di Chrome

    # Navigate to the login page

    # resources = driver.find_elements(By.CSS_SELECTOR, "a.stockBarButton")
    #
    # for resource in resources:
    #     try:
    #         resource_name = resource.find_element(By.CSS_SELECTOR, "i").get_attribute("class")
    #         resource_quantity = int(resource.find_element(By.CSS_SELECTOR, ".value").text)
    #         print(resource_name, resource_quantity)
    #     except ValueError:
    #         print("Errore nella conversione della risorsa")
    #         continue
    #
    #     # Recuperiamo la capacità massima del magazzino
    #     try:
    #         capacity_text = driver.find_element(By.CSS_SELECTOR, ".capacity .value").text
    #         capacity_text = capacity_text.replace('\u202d', '').replace('\u202c', '')
    #         capacity = int(capacity_text)
    #         print(capacity)
    #     except ValueError:
    #         print("Errore nella conversione della capacità massima in intero!")
    #         continue
    #
    #
    #     # Verifichiamo se la quantità supera la capacità massima del magazzino
    #     if resource_quantity >= capacity:
    #         print(f"Il {resource_name} ha superato la capacità massima del magazzino!")
    #     else:
    #         print(f"Il {resource_name} non ha superato la capacità massima del magazzino!")
    print('Login effettuatoo')
    session = requests.Session()
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'])
    while True:
        ampliaCampi(session, driver)
        startAdventure(session,driver)
        time.sleep(10*60)
    #cookies = {cookie["name"]: cookie["value"] for cookie in driver.get_cookies()}
    # session = requests.Session()
    # for cookie in driver.get_cookies():
    #     session.cookies.set(cookie['name'], cookie['value'])
    #
    # for id in range(1, 19):
    #     for gid in range(1, 5):
    #         url = f"https://ts8.x1.europe.travian.com/build.php?id={id}&gid={gid}"
    #         #url = "https://ts8.x1.europe.travian.com/build.php?id=3&gid=1"
    #         response = session.get(url)
    #         #print(response.content)
    #         if response.status_code == 200:
    #             try:
    #                 driver.get(response.url)
    #                 build_button = driver.find_element("xpath", "//button[contains(text(),'Amplia al livello')]")
    #                 build_button.click()
    #             except NoSuchElementException:
    #                 print("Il bottone non è stato trovato")
    #                 continue
def ampliaCampi(session,driver):
    for id in range(1, 19):
        for gid in range(1, 5):
            url = f"https://ts9.x1.europe.travian.com/build.php?id={id}&gid={gid}"
            response = session.get(url)
            if response.status_code == 200:
                try:
                    driver.get(response.url)
                    build_button = driver.find_element("xpath", "//button[contains(text(),'Amplia al livello')]")
                    build_button.click()
                except NoSuchElementException:
                    print("Il bottone non è stato trovato")
                    continue
            time.sleep(10)
        time.sleep(10)
        
def startAdventure(session,driver):
    url = "https://ts9.x1.europe.travian.com/hero/adventures"
    response = session.get(url)
    if response.status_code == 200:
        driver.get(response.url)
        time.sleep(5)
        explore_button = driver.find_element(By.CLASS_NAME, "textButtonV2")
        explore_button.click()
        # # Cicla su tutte le righe della tabella
        # for row in adventure_rows:
        #     # Trova il pulsante "Inizia avventura" nella riga corrente
        #     print(row)
        #     start_button = row.find_element(By.XPATH, ".//button[contains(text(), 'Esplora')]")
        #
        #     # Clicca sul pulsante "Inizia avventura"
        #     start_button.click()
        #
        #     # Attendi il caricamento della pagina successiva
        #     time.sleep(2)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
