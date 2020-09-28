import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
file_name = "counter.html"
driver = webdriver.Chrome(pathlib.Path(os.path.abspath("chromedriver.exe")))

driver.get("https://tienganhmoingay.com")
loginPopup = driver.find_element_by_xpath("""//*[@id="page-container"]/header/div/div[3]/div[2]/ul/li[1]/a""")
loginPopup.click()
inputEmail = driver.find_element_by_xpath("""//*[@id="email1"]""")
inputEmail.send_keys('anhln.vccorp@gmail.com')
inputPass = driver.find_element_by_xpath("""//*[@id="password1"]""")
inputPass.send_keys('Media123+')
inputSubmit = driver.find_element_by_xpath("""//*[@id="submit1"]""")
inputSubmit.click()

class WebpageTests(unittest.TestCase):
    def setUp(self):
        driver.get("https://tienganhmoingay.com")

    def login(self):
        driver.get("https://tienganhmoingay.com")
        loginPopup = driver.find_element_by_xpath("""//*[@id="page-container"]/header/div/div[3]/div[2]/ul/li[1]/a""")
        loginPopup.click()
        inputEmail = driver.find_element_by_xpath("""//*[@id="email1"]""")
        inputEmail.send_keys('anhln.vccorp@gmail.com')
        inputEmail = driver.find_element_by_xpath("""//*[@id="password1"]""")
        inputEmail.send_keys('Media123+' + Keys.RETURN)
    
    # def test_title(self):
    #     driver.get(file_uri(file_name))
    #     self.assertEqual(driver.title, "Counter")
    
    # def test_increase(self):
    #     driver.get(file_uri(file_name))
    #     increase = driver.find_element_by_id("increase")
    #     increase.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")
    
    # def test_decrease(self):
    #     driver.get(file_uri(file_name))
    #     decrease = driver.find_element_by_id("decrease")
    #     decrease.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")
    
    # def test_mutiple_increase(self):
    #     driver.get(file_uri(file_name))
    #     increase = driver.find_element_by_id("increase")
    #     for i in range(3):
    #         increase.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
    
    # def test_mutiple_decrease(self):
    #     driver.get(file_uri(file_name))
    #     decrease = driver.find_element_by_id("decrease")
    #     for i in range(3):
    #         decrease.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "-3")

if __name__ == "__main__":
    unittest.main()