######################## APPLICATION COMMANDS ################################
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

# TITLE
# Obtiene el título de la página
title = driver.title
print(title)

# CURRENT_URL
# Obtiene el link de la página
current_url = driver.current_url
print(current_url)

# PAGE_SOURCE
# Obtiene el codigo fuente de la página
page_source = driver.page_source
print(page_source)

driver.close()
