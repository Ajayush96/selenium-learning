import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class JavaScriptExecution():

    def test1(self):
        # baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.implicitly_wait(3)
        driver.execute_script("window.location ='https://courses.letskodeit.com/practice';")

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


ff = JavaScriptExecution()
ff.test1()
