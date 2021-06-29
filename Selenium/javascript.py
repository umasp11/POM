from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.execute_script("window.open('https://www.yatra.com/', '_self')")

#To pass value to textbox
driver.executeScript("document.getElementById('User').value='testing1'")

#to scroll up/down webpage
driver.execute_script("window.scrollby(0,250)")

#to scroll bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#return druiver title
driver.execute_script("return document.title")

#genrate an alert
driver.execute_script("alert('this is an alert')")