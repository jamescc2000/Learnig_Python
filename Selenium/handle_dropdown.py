from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
#driver.implicitly_wait(10)
sleep(10)
drp_country_element = driver.find_element(By.XPATH, "//select[@id='input-country']")
drp_country = Select(drp_country_element)

# Seleccionar una opcion del DropDown
drp_country.select_by_visible_text("Peru")
drp_country.select_by_value("167")
drp_country.select_by_index(166)

# Obtener todos lo valores del dropdown
all_options = drp_country.options

for option in all_options:
    print(option.text)

# Seleccionar los valores del dropdown sin usar metodos built-in
for option in all_options:
    if option.text == 'Peru':
        option.click()
        break
