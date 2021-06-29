"""
Implicit wait
It will wait for the given time until the element is found, if element is not found after the given time, it will throw nosuchelement exception error. If element is found in 5 sec it wont for the next 15 sec, it will jump to the next line of code.
Implicit wait will used for onetime and it will be applicable for all the webelament

EXPLICIT WAIT:
Is used to tell the webdriver to wait for certain conditions(Expected conditions) to occur before proceeding further with execution.
wait= webdriverwait(driver, 10)

Fluent Wait: it defines the max time to wait for condition along with  need to specify the frequencywith which to check the condition here
wait= webdriverwait(driver, 10, poll frequency=2 sec, ignored_exceptions=[elementInerceptdException])
"""
from selenium.webdriver.common import by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

wait=WebDriverWait(driver,10)
wait.until(ec.element_to_be_clickable(driver.find_elements_by_xpath("add xpath here"))).click()
