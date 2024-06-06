#################################### CONDICIONAL COMMANDS ###################
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")

search_box = driver.find_element(By.XPATH, '//input[@id="small-searchterms"]')

### IS_DISPLAYED
# Si el elemento se encuentra dentro de la pagina retorna True, caso contrario retorna False
if search_box.is_displayed():
    print("The Search box is displayed")
else:
    print("The Search box is NOT displayed")

### IS_ENABLED
# Si el elemento está habilitado (se puede usar) devuelve True, caso contrario devuelve False
if search_box.is_enabled():
    print("The Search box is enabled")
else:
    print("The Search box is NOT enabled")

### IS_SELECTED
# Verifica si un elemento está seleccionado, se usa mayormente para radio buttons y check boxes
male_radio_button = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
female_radio_button = driver.find_element(By.XPATH, '//input[@id="gender-female"]')

if male_radio_button.is_selected():
    print("The male radio button is selected")
elif female_radio_button.is_selected():
    print("The female radio button is selected")
else:
    print('No radio button is selected')
