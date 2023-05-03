from flask import Flask



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
    print('sono qui')
    return "sono qui"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
