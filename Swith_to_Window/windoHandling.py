import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from advance.Genric_screenshot import Screenshot


class SwitchToWindow():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find parent handle -> main Window
        parentHandle = driver.current_window_handle
        print("parent handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles
        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
                searchBox.send_keys("Python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle

        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successfully")
        time.sleep(2)
        Screenshot.takeScreenshot(driver)


ff = SwitchToWindow()
ff.test()
