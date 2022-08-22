import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class slider():

    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # first need to jump in frame

        driver.switch_to.frame(0)
        elemnt = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(elemnt, 100, 0).perform()
            print("sliding element successfully")
            time.sleep(2)
        except:
            print("sliding failed on element")


ff = slider()
ff.test()
