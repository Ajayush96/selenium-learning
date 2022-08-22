from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class ElementState():

    def isEnable(self):
        baseUrl = "https://www.google.com"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
        e1.send_keys("testing")


e = ElementState()
e.isEnable()
