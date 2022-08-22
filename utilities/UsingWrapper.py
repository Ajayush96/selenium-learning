import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities.handyWrapper import HandyWrappers


class usingWrapper():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)

        driver.get(baseUrl)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField1 = hw.getElement("//input[@id='name]", locatorType="xpath")
        textField1.clear()


ff = usingWrapper()
ff.test()
