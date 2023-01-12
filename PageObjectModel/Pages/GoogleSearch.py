import time
from selenium.webdriver.common.by import By


url = "https://www.google.com/"


class GoogleSearch:
    def __init__(self, driver):
        self.driver = driver
        self.search = "gLFyf"
        self.buttonsearch = "btnK"
        self.link1 = "/html/body/div[7]/div/div[11]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/a/div[1]/span"

    def get_search(self):
        return self.driver.find_element(By.CLASS_NAME, self.search)

    def text_search(self, search):
        self.get_search().send_keys(search)
        time.sleep(4)

    def get_buttonsearch(self):
        return self.driver.find_element(By.NAME, self.buttonsearch)

    def click_buttonsearch(self):
        self.get_buttonsearch().click()

    def get_link1(self):
        return self.driver.find_element(By.XPATH, self.link1)

    def click_firtslink(self):
        self.get_link1().click()

    @staticmethod
    def get_url():
        return url
