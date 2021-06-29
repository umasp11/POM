# action.drag_and_drop_by_offset(source, xoffset, yoffset)
# action.click_and_hold(elemnt).pause(second).move_by_offset(xoffset, yoffset).release().perform()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())


left=driver.find_element_by_xpath('left xpath')
right=driver.find_element_by_xpath('right xpath')
action= ActionChains(driver)
action.drag_and_drop_by_offset(left, 50, 0).perform()           # in x direction it will move 50 pIxels to right and y direction 0 pixel
action.drag_and_drop_by_offset(right, -50, 0).perform()         # It will move to left direction as we give value in -ve (x-y axis logic)