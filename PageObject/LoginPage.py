class Login:

    username_id= 'txtUsername'
    password_id= 'txtPassword'
    login_id = 'btnLogin'

    def __init__(self, driver):     #Constructor will initialize the driver, bcz diver need to implement the action method for all element
        self.driver=driver          #it will catch the drivr frm test case and it will pass it frm test case.this drivr will initiate the class variable


    def SetUsername(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def SetPassword(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def Login_button(self):
        self.driver.find_element_by_id(self.login_id).click()
