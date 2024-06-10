import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

all_links = driver.find_elements(By.TAG_NAME, "a")
count = 0
broken_links = []
ok_links = []

for link in all_links:
    # Obtenemos el url
    url = link.get_attribute('href')

    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(f'{url} is broken link')
        count += 1
        broken_links.append(url)
    else:
        ok_links.append(url)
        print(f'{url}is valid link')

