import unittest
import os
from Config.browserdrivers import install_driver
import pdb

# Webdriver Configuration
class WebDriverConf(unittest.TestCase):

    def setUp(self):
        #pdb.set_trace()
        print(os.environ['BROWSER_NAME'])
        self.browser_name = os.environ['BROWSER_NAME']
        #print(type(self.browser_name))
        self.driver = install_driver(self.browser_name.upper())
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
