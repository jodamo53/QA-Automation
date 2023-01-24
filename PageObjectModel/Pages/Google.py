import time
from selenium.webdriver.common.by import By



url = "https://www.google.com/"

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.text_to_search = "Test Automation"
        self.text_to_confirm = "automation"
        self.search_query = "q"
        self.buttonsearch = "btnK"
        self.link1 = ".hlcw0c:nth-child(1) .LC20lb"
        self.link2 = ".g:nth-child(7) .LC20lb"
        self.link3 = ".MjjYud:nth-child(4) .LC20lb"


    def get_search(self):
        return self.driver.find_element(By.NAME, self.search_query)


#Do click on Button Search
    def click_buttonsearch(self):
        self.get_search().send_keys(self.text_to_search)
        time.sleep(2)
        self.driver.find_element(By.NAME, self.buttonsearch).click()
        return True

#Confirm that word "automation" exits in the first link
    def get_link1(self):
        print("\n" + self.driver.find_element(By.CSS_SELECTOR, self.link1).text)
        assert (self.text_to_confirm in self.driver.find_element(By.CSS_SELECTOR, self.link1).text.lower())

#Confirm that word "automation" exits in the second link
    def get_link2(self):
        print(self.driver.find_element(By.CSS_SELECTOR, self.link2).text)
        assert (self.text_to_confirm in self.driver.find_element(By.CSS_SELECTOR, self.link2).text.lower())

# Confirm that word "automation" exits in the third link
    def get_link3(self):
        print(self.driver.find_element(By.CSS_SELECTOR, self.link3).text)
        assert (self.text_to_confirm in self.driver.find_element(By.CSS_SELECTOR, self.link3).text.lower())

#Do click in the first link before searched the "Test Automation" word
    def click_firtslink(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link1).click()

#Confirm that the word "automation" exits in the title page
    def get_text_to_confirm(self):
        self.get_title = self.driver.title
        print("\n" + self.get_title)
        assert (self.text_to_confirm in self.get_title.lower())

    @staticmethod
    def get_url():
        return url
