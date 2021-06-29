from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())


# swith with locator
driver.switch_to_frame(driver.find_elements_by_xpath("ad xpath here"))

# Switch with ID
driver.switch_to_frame('olxframe')

#switch with name
driver.switch_to_frame('olxframe')

#switch with index
driver.switch_to_frame(0)
