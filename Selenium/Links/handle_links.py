from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")

#driver.find_element(By.LINK_TEXT, 'Digital downloads').click()

# Usando XPATH
links = driver.find_elements(By.XPATH, '//a')
print(len(links))

# Usando TAG_NAME
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

# Mostrar todos los links
for link in links:
    print(link.text)