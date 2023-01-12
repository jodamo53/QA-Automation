
import time
from PageObjectModel.Pages import GoogleSearch
from PageObjectModel.Config.WebDriverConf import WebDriverConf
from PageObjectModel.Pages.GoogleSearch import GoogleSearch


class test_Scenario(WebDriverConf):


    def test_scenario1(self):
         driver = self.driver
         self.driver.get(GoogleSearch.get_url())
         google_search = GoogleSearch(driver)
         time.sleep(2)
         google_search.text_search("Test Automation")
         google_search.click_buttonsearch()

   




