"""
Download python. Goto script folder and copy the folder path
go to system environment variable and add this python path

whille creating project in pycharm, select env as virtual env

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.yatra.com/')

#get cookies
cookies=driver.get_cookies()

#Add cookies
driver.add_cookie({'name':'umasankar', "domain":'yatra.com', 'value':'python'})

print(cookies)