from PageObjectModel.Pages import Google
from PageObjectModel.Config.WebDriverConf import WebDriverConf
from PageObjectModel.Pages.Google import Google



class test_Scenario(WebDriverConf):
     def test_scenario1(self):
           driver = self.driver
           self.driver.get(Google.get_url())
           google_search = Google(driver)
           google_search.click_buttonsearch()
           google_search.get_link1()
           google_search.get_link2()
           google_search.get_link3()

   




