from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_driver():
    #configuración de opera
    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    time.sleep(5)

    return driver

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def login_sauce(driver):
    # driver = get_driver()
    #obtener url
    driver.get(URL)

    #ingresar user name
    driver.find_element(By.ID,'user-name').send_keys(USERNAME)
    #ingresar password
    driver.find_element(By.ID,'password').send_keys(PASSWORD)
    #captura el boton y hace click
    driver.find_element(By.NAME,'login-button').click()

    time.sleep(7)
    
    #busco que despues de loguear me lleve a "" en el url
    return "/inventory.html" in driver.current_url and driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text == 'Products'
    
    
   


