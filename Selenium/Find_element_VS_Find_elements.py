from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

### FIND_ELEMENT
# Devuelve un solo elemento

# 1) locator coincide con un solo elemento
element = driver.find_element(By.XPATH, '//input[@id="small-searchterms"]')
element.send_keys('laptop')

# 2) locator coincide con varios elementos
# Devuelve solo el primer elemento que encuentra
element = driver.find_element(By.XPATH, '//div[@class="footer"]//a')
print(element.text)

# 3) Si el elemento no es encontrado lanza el erro de NoSuchElementException


### FIND_ELEMENTS
# Siempre retorna una lista de items

# 1) locator coincide con un solo elemento
elements = driver.find_elements(By.XPATH, '//input[@id="small-searchterms"]')
elements[0].send_keys('MacBook')

# 2) locator coincide con varios elementos
elements = driver.find_elements(By.XPATH, '//div[@class="footer"]//a')
for element in elements:
    print(element.text)

# 3) Si el elemento no es encontrado
# No devuelve un error, sino que devuelve una lista vaciá
login_element = driver.find_elements(By.LINK_TEXT, 'Log')
print(login_element)


