from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

### SELF
# Es el mismo elemento que se desea buscar
# Nota: no es necesario usar /self::tag_name
print('-------------------- SLEF ------------------------')
self_text_msg = driver.find_element(By.XPATH, '//a[contains(text(),"JTL Industries")]/self::a').text
print(self_text_msg)
print('--------------------------------------------------')

### PARENT
# Es el elemento anterior al actual
print('-------------------- PARENT -----------------------')
parent_text_msg = driver.find_element(By.XPATH, '//a[contains(text(),"JTL Industries")]/parent::td').text
print(parent_text_msg)
print('---------------------------------------------------')

### ANCESTOR
print('-------------------- ANCESTOR -----------------------')
# Es el elemento anterior del anterior del actual
ancestor_text_msg = driver.find_element(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr').text
print(ancestor_text_msg)
print('-----------------------------------------------------')

### CHILD
# Es el elemento posterior al actual
# En este caso partimos del ancestor porque el elemento actual (self) no tiene childs
childs_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/child::td')

print('-------------------- CHILDS -----------------------')
for child in childs_text_msg:
    print(child.text)
print('----------------------------------------------------')

### DESCENDANT
descendats_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/descendant::*')

print('-------------------- DESCENDANT -----------------------')
for descendat in descendats_text_msg:
    print(descendat.text)
print('-------------------------------------------------------')

### FOLLOWING
followings_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/following::*')

print('-------------------- FOLLOWING -----------------------')
print(f'There are {len(followings_text_msg)} followings nodes')
print('-------------------------------------------------------')

### FOLLOWING-SIBLING
following_siblings_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/following-sibling::*')

print('-------------------- FOLLOWING-SIBLING -----------------------')
for following_sibling in following_siblings_text_msg:
    print(following_sibling.text)
print('--------------------------------------------------------------')

### PRECEDING
precedings_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/preceding::tr')

print('-------------------- PRECEDING -----------------------')
for precedent in precedings_text_msg:
    print(precedent.text)
print('------------------------------------------------------')

### PRECEDING-SIBLING
preceding_siblings_text_msg = driver.find_elements(By.XPATH, '//a[contains(text(),"JTL Industries")]/ancestor::tr/preceding-sibling::tr')

print('-------------------- PRECEDING-SIBLINGS -----------------------')
for precedent in preceding_siblings_text_msg:
    print(precedent.text)
print('------------------------------------------------------')


driver.close()
