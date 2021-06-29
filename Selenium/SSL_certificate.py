#option.add_argument("--allow-running-insecure-content")
#option.add_argument("--ignore-certificate-errors")

#Another method
#option.set_capability("acceptInsecureCerts", True)
#driver= webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

option= Options()
option.add_argument("--allow-running-insecure-content")
option.add_argument("--ignore-certificate-errors")
#driver= webdriver.Chrome(ChromeDriverManager().install(), options=option)

#another method
option.set_capability("acceptInsecureCerts", True)
#driver= webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

#Firefox
profile=webdriver.FirefoxProfile()
profile.accept_untrusted_certs=True

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)

driver.get('url')
