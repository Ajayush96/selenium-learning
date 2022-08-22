import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from wait_types.explicit_wait_type import ExplicitWaitType


class ExplicitWaitDemo2():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//a[contains(text(),'Sign In')]",
                                      locatorType="xpath")
        element.click()

        # LoginLink = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
        # LoginLink.click()


ff = ExplicitWaitDemo2()
ff.test()
