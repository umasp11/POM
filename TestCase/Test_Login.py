import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from Utilities.ReadProperties import ReadConfig

class Test_Login:
    url= ReadConfig.getappurl()
    username= ReadConfig.getusername()
    password= ReadConfig.getpassword()

    def test_HomePage_Title(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        title=self.driver.title
        assert title== 'OrangeHRM'
        self.driver.close()

    def test_001_Login(self,setup):
        self.driver = setup                     #Setup method will return the driver and it will be assigned to driver variable
        self.driver.get(self.url)
        self.lp_obj=Login(self.driver)           #created object for Loginpage object class
        self.lp_obj.SetUsername(self.username)
        self.lp_obj.SetPassword(self.password)
        self.lp_obj.Login_button()
        title= self.driver.title
        self.driver.close()
        assert title== 'OrangeHRM'