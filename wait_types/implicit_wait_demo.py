from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        LoginLink = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
        LoginLink.click()

        EmailField = driver.find_element(By.XPATH, "//input[@id='email']")
        EmailField.send_keys("ajayush96@gmail.com")


ff = ImplicitWaitDemo()
ff.test()
