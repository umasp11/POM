"""
Create login page object class under "pageobjects" folder
Create login test under test case
create conftest.py under test case--- put the commomon things here


Page object folder:
1) create loginpage object means create a loginpage python file
2) create a class with name as class login
3) create a constructor method to initialize the driver
4) create action method for all the elements like username, password, login

Testcase folder:
1) create a logintest folder test_login.py
2) Import pytest, selenium and pageobject module
3) create class and  assign value to  url, username, password
4) create testcase methods and create driver method under this      (creating driver is duplicated in every method so for this will create conftest.py)
5) now to access page object element, call the page object class i.e create object of login_page class

Create conftest.py file under testcase folder
1) here add pytest.fixture method say method name is setup()
2) call this method in test case folder under test method


configuration folder
in test case folder we saw url, username, password for login class. It will be used for other test calss as well so we need to call it again and again.
it will be very repititive and we should not hardcode this data. we will save this in .ini file under configuration folder
add the data in this .ini file by categorizing like [login info], [common data]



Utilities Folder
create readProperties.py file to read the common data from .ini file
import configparse library and crete object for configparser.RawConfigParser()
Create class Readocnfig and then create static method for all the data like url, username, password.
we created static method for all the data cause when we will call this method in test case no need to create object for this
then in testcase folder import this file and class Readconfig
call the method in url, username field


"""

import pytest

test_data= [(3,5,8), (20,40,60), (40,50,90)]
@pytest.mark.parametrize("ip,op,to", test_data)
def test_calculator(ip, op, to):
    assert ip+op==to


import pytest


# using fixture
@pytest.fixture(params=["a", "b"])
def demo(request):
    print(request.param)


def test_login(demo):
    print('login successfull')
