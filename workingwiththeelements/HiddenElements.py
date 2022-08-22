import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class HiddenElements():

    def testListOfElements(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # find the state of  the text box

        textBoxElement = driver.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed()  # true if visible else false
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))

        time.sleep(2)

        # click the hide button

        driver.find_element(By.ID,"hide-textbox").click()
        time.sleep(2)
        # find the state of text box
        textBoxState = textBoxElement.is_displayed()  # true if visible else false
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)
        # Click the Show button

        driver.find_element(By.ID,"show-textbox").click()
        time.sleep(2)
        # Find the state of the text box

        textBoxState = textBoxElement.is_displayed()  # true if visible else false
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)
        # browser close

        driver.close()

    # def testExpedia(self):
    #     baseUrl = "www.expedia.com"
    #     serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")
    #
    #     driver = webdriver.Chrome(service=serv_obj)
    #     driver.maximize_window()
    #     driver.get(baseUrl)
    #     driver.implicitly_wait(10)


ff = HiddenElements()
ff.testListOfElements()
