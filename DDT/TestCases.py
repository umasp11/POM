from DDT import XLUtils
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://demo.guru99.com/test/newtours/index.php')
driver.maximize_window()

path= "C:\\Users\\umasankar.panigrahy\Desktop\Docker\PM\Login.xlsx"

rows= XLUtils.getRowCount(path,"Sheet1")
for r in range(2,rows+1):
    username=XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

    if driver.title=='Login: Mercury Tours':
        print('test is passed')
        XLUtils.writeData(path,'Sheet1',r,3, 'Pass')
    else:
        print('test is Failed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Fail')
    driver.find_element_by_link_text("Home").click()
