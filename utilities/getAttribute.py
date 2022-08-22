import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class GetText():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "name")
        result = element.get_attribute("class")

        print("value of attribute is: " + result)

        element1 = driver.find_element(By.ID, "openwindow")
        result1 = element1.get_attribute("onclick")

        print("value of attribute is: " + result1)

        time.sleep(2)
        driver.quit()


ff = GetText()
ff.test()
