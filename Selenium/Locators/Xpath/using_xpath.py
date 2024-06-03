from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

### Absolute XPATH
# El absolute xpath esta basada en la DOM structure de la pagina web
# La estructura es la siguiente html/tag1/tag2/tag3[indice]/tag4/tag5[indice]/tag6
# Nota: cuando el tag tiene un [] con un numero n adentro, significa que existen varios tag y esta elijiendo el n-esimo tag
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[2]/form/input').send_keys("Apple MacBook Pro")

# Relative XPATH
# Es la mas recoendad para hacer busqueda de elementos debido a su estabilidad
# La estrucutra es la siguiente: //tag_name[@attribute="value"]
# Nota 1: Si no se conoce el tag_name se puede cambiar por *
# Nota 2: al relative xpath se le puede agregar partes de un absolute xpath
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()

sleep(2)

# AND
driver.find_element(By.XPATH, '//*[@type="button" and @class="button-2 product-box-add-to-cart-button"]').click()

sleep(3)

# OR
driver.find_element(By.XPATH, '//*[@id="add-to-cart-button-4" or @class="button-1 add-to-cart-button"]').click()

# START_WITH()
# Busca el elemento, cuyo atributo empieze con el valor especificado
driver.find_element(By.XPATH, '//*[starts-with(@id, "add-to-wishlist")]').click() # El nombre completo del id es "add-to-wishlist-button-4"

# CONTAINS()
# Busca el elemento, cuyo atributo contengan el valor especificado
driver.find_element(By.XPATH, '//button[contains(@class, "email-a-friend")]').click() # El nombre completo de la clase es "button-2 email-a-friend-button"

sleep(2)

# TEXT()
# Busca el texto que esta dentor del tag
driver.find_element(By.XPATH, '//span[text()="Shopping cart"]').click()