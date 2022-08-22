import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class JavaScriptExecution():

    def test1(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Height: " + str(height))
        print("Width: " + str(width))
        driver.quit()


ff = JavaScriptExecution()
ff.test1()
