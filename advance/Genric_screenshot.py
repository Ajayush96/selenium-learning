import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Screenshot():

    def test1(self):
        baseUrl = "https://courses.letskodeit.com/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        LoginLink = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
        LoginLink.click()

        EmailField = driver.find_element(By.XPATH, "//input[@id='email']")
        EmailField.send_keys("ajayush96@gmail.com")

        PassField = driver.find_element(By.ID, "password")
        PassField.send_keys("gddgdqgd8687687")

        LoginButton = driver.find_element(By.XPATH, "//input[@value='Login']")
        LoginButton.click()
        self.takeScreenshot(driver)

    #@staticmethod
    def takeScreenshot(self,driver):
        """
        Take screenshot of the current open web page
        :param driver:\
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"  # generation random charecter
        screenshotDirectory = "/home/stinger/Desktop/"
        destinationFileName = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to the directory ::" + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshot()
ff.test1()

