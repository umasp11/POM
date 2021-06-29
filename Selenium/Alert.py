from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



option= Options()
option.add_argument("--disable-notifications")      # to block browser notification popup
driver= webdriver.Chrome(ChromeDriverManager().install(), options=option)

driver.get('https://www.yatra.com/')




"""
#Accept alert
driver.switch_to_alert().accept()

#Dismiss alert
driver.switch_to_alert().dismiss()

#send text to alert
driver.switch_to_alert().send_keys('umasankar')
driver.switch_to_alert().accept()
"""