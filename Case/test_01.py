from selenium import webdriver
from Common.Input_page import Base
from selenium.webdriver.common.by import By
import time
import unittest

class Test_Input(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.b =Base(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_input_text(self):
        x =(By.ID,"kw")
        self.b.input_text(x, "组合")
        time.sleep(5)

