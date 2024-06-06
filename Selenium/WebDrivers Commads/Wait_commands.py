######################################### WAIT COMMANDS ########################################
from time import sleep
from selenium import webdriver
from selenium.common import ElementNotSelectableException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# IMPLICITLY_WAIT
# Se indica al inicio del programa
# Es aplicable para todo los comandos siguientes
# El tiempo especificado es el tiempo maximo que se esperara y no necesariamente el tiempo total que tomara
driver.implicitly_wait(10)


# EXPLICIT WAIT
# Se declara el objeto y se especifica el timpo maximo de espera para que se cumpla alguna condicion dada
# Tambien se peude especificar cada cuanto tiempo se verifica que se cumpla la condicion con poll_frecuency
# Tambien se peude especificar que errores manejar si es que no se cumplió la condicion despues del tiempo maximo
mywait = WebDriverWait(driver, 10, poll_frequency=2,ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception])


driver.get("https://www.google.com/")
driver.maximize_window()

buscador = driver.find_element(By.XPATH, '//textarea[@id="APjFqb"]')
buscador.send_keys('Selenium')
buscador.submit() # Envia la tecla enter

# SLEEP
# No es la mas recomendada debido a que reduce mucho el rendimiento del programa
# Ademas, puede que el elemento, despues del tiempo especificado, aun no se encuentre disponible
sleep(1)

# EXPLICIT WAIT
# Se especifica la condicion con EC (expected_condition) y esta esperara que se cumpla la condicion hasta el tiempo especificado inicialmente
mywait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))

driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()

driver.quit()
