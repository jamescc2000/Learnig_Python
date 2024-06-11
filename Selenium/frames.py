from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www3.animeflv.net/ver/tsuki-ga-michibiku-isekai-douchuu-2nd-season-23")

video = driver.find_element(By.XPATH, "//iframe[contains(@src,'mega')]")
link = video.get_attribute("src").replace('embed', '')
print(link)

driver.find_element(By.XPATH, "//a[contains(@href,'option1')]").click()

video = driver.find_element(By.XPATH, "//iframe[contains(@src,'streamwish')]")
link = video.get_attribute("src").replace('/e/', '/d/')
print(link)

driver.find_element(By.XPATH, "//a[contains(@href,'option6')]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar y Continuar']").click()
sleep(3)
video = driver.find_element(By.XPATH, "//iframe[contains(@src,'streamtape')]")
link = video.get_attribute("src")
print(link)

######################################################################################################################

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outter_frame = driver.find_element(By.XPATH, "//iframe[contains(@src,'MultipleFrames.html')]")
driver.switch_to.frame(outter_frame)

inner_frame = driver.find_element(By.XPATH, "//iframe[contains(@src,'SingleFrame.html')]")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")



# Vuelve a  la pagina principal
#driver.switch_to.default_content()
