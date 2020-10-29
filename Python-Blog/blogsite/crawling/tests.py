import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
file_name = "counter.html"
chrome_path = pathlib.Path(os.path.abspath("chromedriver.exe"))
print(chrome_path)
driver = webdriver.Chrome(chrome_path)


driver.get("https://tienganhmoingay.com")
driver.implicitly_wait(10)
loginPopup = driver.find_element_by_xpath("""//*[@id="page-container"]/header/div/div[3]/div[2]/ul/li[1]/a""")
loginPopup.click()
driver.implicitly_wait(10)
inputEmail = driver.find_element_by_xpath("""//*[@id="email1"]""")
inputEmail.send_keys('anhln.vccorp@gmail.com')
inputPass = driver.find_element_by_xpath("""//*[@id="password1"]""")
inputPass.send_keys('Abc123456')
inputSubmit = driver.find_element_by_xpath("""//*[@id="submit1"]""")
inputSubmit.click()

driver.implicitly_wait(100)
# open menu
expanMenu = driver.find_element_by_class_name("chart-button")
expanMenu.click()
print('open link')
driver.implicitly_wait(300)
viewAllRutGon = driver.find_element_by_xpath("""//*[@id="detoeic_rutgon"]/a[2]""")
viewAllRutGon.click()

# driver.close()

# class WebpageTests(unittest.TestCase):
#     def login(self):
#         driver.get("https://tienganhmoingay.com")
#         driver.implicitly_wait(10) 
#         loginPopup = driver.find_element_by_xpath("""//*[@id="page-container"]/header/div/div[3]/div[2]/ul/li[1]/a""")
#         loginPopup.click()
#         driver.implicitly_wait(10) 
#         inputEmail = driver.find_element_by_xpath("""//*[@id="email1"]""")
#         inputEmail.send_keys('anhln.vccorp@gmail.com')
#         inputPass = driver.find_element_by_xpath("""//*[@id="password1"]""")
#         inputPass.send_keys('Abc123456')
#         inputSubmit = driver.find_element_by_xpath("""//*[@id="submit1"]""")
#         inputSubmit.click()
#         self.assertEqual(driver.title, "Luyện thi TOEIC Online Hiệu quả nhất | Tiếng Anh Mỗi Ngày")
        
#         driver.implicitly_wait(60) 
#         driver.close()
    
#     # def test_title(self):
#     #     driver.get(file_uri(file_name))
#     #     self.assertEqual(driver.title, "Counter")
    
#     # def test_increase(self):
#     #     driver.get(file_uri(file_name))
#     #     increase = driver.find_element_by_id("increase")
#     #     increase.click()
#     #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")
    
#     # def test_decrease(self):
#     #     driver.get(file_uri(file_name))
#     #     decrease = driver.find_element_by_id("decrease")
#     #     decrease.click()
#     #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")
    
#     # def test_mutiple_increase(self):
#     #     driver.get(file_uri(file_name))
#     #     increase = driver.find_element_by_id("increase")
#     #     for i in range(3):
#     #         increase.click()
#     #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
    
#     # def test_mutiple_decrease(self):
#     #     driver.get(file_uri(file_name))
#     #     decrease = driver.find_element_by_id("decrease")
#     #     for i in range(3):
#     #         decrease.click()
#     #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "-3")

# if __name__ == "__main__":
#     unittest.main()