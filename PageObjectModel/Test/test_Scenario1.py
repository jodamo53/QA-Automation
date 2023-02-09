
from Config.webdriverconf import WebDriverConf
from Pages.google import Google


class test_Scenario(WebDriverConf):
    def test_scenario1(self):
        driver = self.driver
        self.driver.get(Google.get_url())
        search = Google(driver)
        search.click_buttonsearch()
        search.get_link1()
        search.get_link2()
        search.get_link3()
