"""
for mousehover and sending any keys(tab, enter, page up/down) operation import ActionChains and Key module

Screenshot:
driver.screenshot(".\\test.png") it will store the image of perticular webelement

#It will save screenshot of webpage
driver.get_screenshot_as_file(".\\test1.png")
driver.save_screenshot(".\\test.png")

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element_by_id('txtUsername').send_keys('admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()


action=ActionChains(driver)
admin=driver.find_element_by_xpath("//b[text()='Admin']")
user=driver.find_element_by_xpath("//a[text()='User Management']")
action.move_to_element(admin).move_to_element(user).click().perform()

action.send_keys(Keys.TAB)
action.send_keys(Keys.ENTER)
action.send_keys(Keys.CONTROL).send_keys('a')       #ctrl+a

action.click()      #left click
action.double_click(admin)
action.context_click(user).perform()              #right click
driver.find_element_by_xpath("//a[text()='User Management']").click()