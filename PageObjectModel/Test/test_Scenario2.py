
from Config.webdriverconf import WebDriverConf
from Pages.google import Google


class test_Scenario(WebDriverConf):

    def test_scenario2(self):
        driver = self.driver
        self.driver.get(Google.get_url())
        search = Google(driver)
        search.click_buttonsearch()
        search.click_firtslink()
        search.get_text_to_confirm()
