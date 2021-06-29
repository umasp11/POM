from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.yatra.com/')
source=driver.find_element_by_id("BE_flight_origin_city")
source.click()
source.send_keys('New Delhi')
source.send_keys(Keys.ENTER)
arrival=driver.find_element_by_id("BE_flight_arrival_city").send_keys('new')
search_list= driver.find_element_by_xpath("//div[@class='viewport']//div//div[1]/li[2]").click()

#we can save the search results in a list and then using for loop we can select one
for result in search_list:
    if 'mumbai' in result.text:
        result.click()
        break