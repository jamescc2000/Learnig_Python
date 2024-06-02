from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome()

# abrimos la pagina
driver.get('https://demo.nopcommerce.com/')
sleep(1)
# Maximizamos la ventana
driver.maximize_window()


###################### Buscando los elementos con los Locators #############################3
### Usando el ID
driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

### Usando el Name
driver.find_element(By.NAME, 'q').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

### Usando el LINK_TEXT
# Es necesario que el valor (texto del enlace) sea exactamente igual al de la página
driver.find_element(By.LINK_TEXT, 'Register').click()

### Usando el PARTIAL_LINK_TEXT
# El valor puede ser una parte del valor (texto del enlace) que está en la página
driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital').click() # En este caso el texto conmpleto del enlace es Digital downloads

### Usando el CLASS_NAME
# Como más de un elemento puede tener la misma clase, se usa find_elements
items = driver.find_elements(By.CLASS_NAME, 'item-box')
print(len(items))

### Usando el TAG_NAME
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

driver.close()
driver2 = webdriver.Chrome()
driver2.get('https://www.facebook.com/')

### Usando CCS_SELECTOR
# En todas las siguientes combinaciones, TAG es opcional

# TAG and ID
# La estructura es la siguiente: nombre_del_tag#valor_del_id
driver2.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc@gmail.com') # el tag es input y el valor del id es email

# TAG and CLASS
# La estructura es la siguiente: nombre_del_tag.valor.de_la.clase (Nota: si la clase lleva espacios en blanco, estos se reemplazan por puntos)
driver2.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy._9npi').send_keys('pass123') # el tag es input y el valor de la clase es inputtext _55r1 _6luy _9npi

# TAG and attribute (cualquier otro atributo)
# La estructura es la siguiente: tag_name[attribute=value]
driver2.find_element(By.CSS_SELECTOR, 'button[data-testid=royal_login_button]').click()

# TAG and CLASS and attribute
# La estrucutra es la siguiente: tag_name.class_name[attribute=value]
driver2.find_element(By.CSS_SELECTOR, 'input.inputtext[aria-label=Password]').send_keys('321ssap')

driver2.close()

