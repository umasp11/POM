"""
Webdriver manager:
this livrary helps Automatic management of browser driver for selenium: automatically browser version, driver path will be handled

xpath: //* and css:* using this we can find out all the webelements in a webpage

Xpath:
starts-with:    //div[starts-with(@class,'header')]
text():         //div[text()='You have no items in your shopping cart.']
contains:       //div[contains(@class,'header')]
Parent:         //div[contains(@class,'header')]//parent::div[@class='master-wrapper-page']
following-sibling:  //a[contains(text(),'feature')]//parent::*following-sibling::li[2]
to get attribute:   .get_attribute('name/type')

In sleneium every webelement is a class
if it returns multiple webelement, datatype will be list

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


#Headless chrome
option=Options()
option.headless=True

driver= webdriver.Chrome(ChromeDriverManager().install(),options=option)

driver.get('https://demo.nopcommerce.com/')
driver.find_element_by_xpath("//a[@class='ico-login']").click()
a=driver.find_element_by_xpath("//input[@class='email']").get_attribute('name')




print(a)
driver.quit()
