import unittest
from selenium import webdriver



#Webdriver Configuration
class WebDriverConf(unittest.TestCase):

    def setUp(self):
        #self.path = 'C:\\Users\\jodam\\PycharmProjects\\QA-Automation\\PageObjectModel\\WebDrivers\\geckodriver-v0.32.0-win64\\geckodriver.exe'
        self.path = 'C:\\Users\\jodam\\PycharmProjects\\QA-Automation\\PageObjectModel\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()