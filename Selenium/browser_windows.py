from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(2)
window_id = driver.current_window_handle
print(window_id)

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
windows_ids = driver.window_handles

parent_window = windows_ids[0]
child_window = windows_ids[1]

driver.switch_to.window(child_window)
print(driver.title)
sleep(3)

driver.switch_to.window(parent_window)
print(driver.title)


for window in windows_ids:
    driver.switch_to.window(window)
    print(driver.title)

for window in windows_ids:
    driver.switch_to.window(window)
    if driver.title == "Human Resources Management Software | OrangeHRM":
        driver.close()

driver.quit()
