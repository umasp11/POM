
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()
parent_handle=browser.get("https://www.google.com")
browser.execute_script("window.open()")
all_handles=browser.window_handles
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.youtube.com")
time.sleep(1)
print(browser.current_window_handle)


for handle in all_handles:
    if handle != parent_handle:
        browser.switch_to_window(handle)
        browser.find_elements_by_xpath("add xpath here")

browser.switch_to_window(parent_handle)