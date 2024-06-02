from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
sleep(1)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print('Login test passed')
else:
    print('Login test failed')

driver.close()