import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities.handyWrapper import HandyWrappers


class ElementPresenceCheck():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementresult = hw.isElementPresent("name", By.ID)
        print(str(elementresult))

        elementresult1 = hw.elementPresenceCheck("//input[@id='name']",By.XPATH)
        print(str(elementresult1))


ff = ElementPresenceCheck()
ff.test()
