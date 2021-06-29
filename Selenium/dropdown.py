"""
if the tag name is select, its dropdown element
to work with dropdown we have to import select class from webdriver
create a object of the dropdown element i.e obj= Select(driver.find_element_id('name'))
select_by_index(2), select_by_value('5'), select_by_visible_text

"""


from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element_by_id('txtUsername').send_keys('admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
time.sleep(2)
driver.find_element_by_xpath("//b[text()='Admin']").click()
obj=Select(driver.find_element_by_id('searchSystemUser_userType'))

obj.select_by_index(1)
obj.select_by_value('2')
obj.select_by_visible_text('Admin')

