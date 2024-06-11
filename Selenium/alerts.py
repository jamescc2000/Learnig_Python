import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Abriendo la alerta
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

# Creando el objeto alerta
alert_window = driver.switch_to.alert
print(alert_window.text)

# Introducion un texto a la alerta
alert_window.send_keys("Welcome")

# Aceptando la alerta
alert_window.accept()

# Cierra la alerta
#alert_window.dismiss()

driver.get(" ")

