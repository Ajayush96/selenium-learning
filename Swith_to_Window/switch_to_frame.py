import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# from advance.Genric_screenshot import Screenshot


class SwitchToFrame():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,900)")

        # switch to frame using I'd
        # driver.switch_to.frame("courses-iframe")

        # switch to frame using name
        driver.switch_to.frame("iframe-name")

        # switch to frame using number
        # driver.switch_to.frame("0")

        time.sleep(2)

        # search course
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-900)")
        time.sleep(2)

        driver.find_element(By.ID, "name").send_keys("Test Successfully")


ff = SwitchToFrame()
ff.test()
