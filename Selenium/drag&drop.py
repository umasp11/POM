# action.drag_and_drop_by(source element, dest element)
#action.drag_and_drop_by_offset(source element, Xoffeset, Yoffset)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())


elem1=driver.find_element_by_xpath('left xpath')
elem2=driver.find_element_by_xpath('right xpath')
action= ActionChains(driver)
action.drag_and_drop_by_offset(elem1, elem2).perform()           # in x direction it will move 50 pIxels to right and y direction 0 pixel
action.drag_and_drop_by_offset(elem1, 50, 150).perform()         # It will move to left direction as we give value in -ve (x-y axis logic)