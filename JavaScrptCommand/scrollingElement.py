import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class ScrollingElement():

    def test1(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Scroll Down
        driver.execute_script("window.scrollBy(0,900)")
        time.sleep(5)

        # Scroll Up
        driver.execute_script("window.scrollBy(0,-900)")
        time.sleep(5)

        # Scroll Element Into View

        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-150)")

        # Native Way To Scroll Element Into View
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-900);")
        location = element.location_once_scrolled_into_view   #it does element scroll into view and then gives back location
        print("Location: " + str(location))
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150)")
        time.sleep(3)




ff = ScrollingElement()
ff.test1()
