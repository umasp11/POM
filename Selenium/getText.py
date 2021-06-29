from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
txt=driver.find_element_by_xpath("//a[contains(text(),'Forgot your password?')]").text
attr=driver.find_element_by_id('btnLogin').get_attribute('name')
enabl=driver.find_element_by_id('txtUsername').is_enabled()
print(enabl)
print(attr)
print(txt)

all_text=driver.execute_script("return document.documentElement.innerText")
print(all_text)
driver.quit()

