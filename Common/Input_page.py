from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

class Base(object):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_element(self, local):
        element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*local))
        return element

    def input_text(self, local, text):
        e = self.find_element(local)
        e.send_keys(text)




