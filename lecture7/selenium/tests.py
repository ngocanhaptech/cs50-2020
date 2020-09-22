import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
file_name = "counter.html"
driver = webdriver.Chrome("chromedriver.exe")

class WebpageTests(unittest.TestCase):
    
    def test_title(self):
        driver.get(file_uri(file_name))
        self.assertEqual(driver.title, "Counter")
    
    def test_increase(self):
        driver.get(file_uri(file_name))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")
    
    def test_decrease(self):
        driver.get(file_uri(file_name))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")
    
    def test_mutiple_increase(self):
        driver.get(file_uri(file_name))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
    
    def test_mutiple_decrease(self):
        driver.get(file_uri(file_name))
        decrease = driver.find_element_by_id("decrease")
        for i in range(3):
            decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-3")

if __name__ == "__main__":
    unittest.main()