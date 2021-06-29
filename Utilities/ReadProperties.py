import configparser

config= configparser.RawConfigParser()        #this method is used to read ini file
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod                           #we can directly call this method in test case, no need to create object for this as itsa a static method
    def getappurl():
        url=config.get('login info', 'url')
        return url

    @staticmethod
    def getusername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('login info', 'password')
        return password
