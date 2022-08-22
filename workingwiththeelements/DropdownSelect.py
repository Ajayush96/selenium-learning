import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


class DropdownSelect():

    def testListOfElements(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.XPATH, "//select[@id='carselect']")
        sel = Select(element)

        sel.select_by_value("benz")
        print("select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("select Honda by index")


ff = DropdownSelect()
ff.testListOfElements()
