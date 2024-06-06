import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
time.sleep(5)

# CLOSE
# Cierre una ventana, pero el programa sigue corriendo en segundo plano
driver.close()

time.sleep(3)

# QUIT
# Cierras definitivamente todas las ventanas o pestañas abiertas
driver.quit()
