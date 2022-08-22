import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MouseHovering():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = "//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            print("Mouse hovered in elemnet")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            action.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover Failed in element")

ff=MouseHovering()
ff.test()
