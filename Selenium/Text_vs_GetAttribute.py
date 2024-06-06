from prompt_toolkit.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://admin-demo.nopcommerce.com/login')

email_box = driver.find_element(By.XPATH, '//input[@id="Email"]')
email_box.clear()
email_box.send_keys('abc@gmail.com')

boton = driver.find_element(By.XPATH, '//button[normalize-space()="Log in"]')

# TEXT
# Solo retorna el inner text del elemento, sino tien, no retorna nada
print('-------------------------------- TEXT -------------------------------------------')
print(f'El resultado para email_box de Text: {email_box.text}')
print(f'El resultado para boton de Text: {boton.text}')
print('----------------------------------------------------------------------------------')

# GET_ATTRIBUTE
# Obtiene el valor de algún artibuto del elemento
print('-------------------------------- GET_ATTRIBUTE -------------------------------------------')
print(f'El resultado para email_box de GetAttribute: {email_box.get_attribute("value")}') # En este caso el email se almacena en el atributo value del elemento input
print(f'El resultado para boton de GetAttribute: {boton.get_attribute("class")}')
print('------------------------------------------------------------------------------------------')