import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        # driver.get(baseUrl)

        driver.execute_script("window.location = 'https://courses.letskodeit.com/';")

        # LoginLink = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
        # LoginLink.click()

        # applying explicit waits

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
        ])

        element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                               "//a[(text()='Sign In')")))
        element.click()


ff = ExplicitWaitDemo()
ff.test()
