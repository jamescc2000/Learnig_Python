import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Para poder autenticarnos con los pop-ups debemos usar la siguiente sintaxis:
# https://username:password@pagename.com
# Con eso injectamos los campos en la url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

driver.quit()