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

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)

        time.sleep(2)
        driver.quit()


ff = GetText()
ff.test()
