import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragAndDrop():

    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # first need to jump in frame

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        topElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(fromElement, topElement).perform()
            actions.click_and_hold(fromElement).move_to_element(topElement).perform()
            print("Drag and drop element successfully")
            time.sleep(2)
        except:
            print("Drag and drop failed on element")


ff = DragAndDrop()
ff.test()
