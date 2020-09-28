import os
import pathlib
import unittest

from selenium import webdriver
import page

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
file_name = "counter.html"




class WebpageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://tienganhmoingay.com")

    def login(self):
        main_page = page.MainPage(self.driver)
        # elem = driver.find_element_by_id("email")
        # print(elem)
        # elem.clear()
        # driver.close()
    
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