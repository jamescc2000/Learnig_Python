######################################## NAVIGATIONAL COMMANDS ###############################################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://pe.ebay.com/")
driver.get("https://www.amazon.com/")

### BACK
# Regresa a la pagina anterior, en este caso regresaria a ebay.com
driver.back()

### FOWARD
# Va a la pagina posterior, en este caso como vovilmos a ebay, ahora iria a amazon.com
driver.forward()

### REFRESH
# Actualzia la pagina actual
driver.refresh()

time.sleep(1)
driver.quit()
