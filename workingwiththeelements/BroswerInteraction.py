from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class BrowserInteractions():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)

        # window maximize

        driver.maximize_window()

        # open the url

        driver.get(baseUrl)

        # Get title

        title =driver.title

        print("title of the page is:" + title)

        # get current url

        curentUrl = driver.current_url

        print("current url of the page is" + curentUrl)

        # Browser ref

        driver.refresh()

        print("ref ist time")

        driver.get(driver.current_url)

        print("ref 2nd time")

        # open another url

        driver.get("https:www.google.com")

        # browser backward

        driver.back()

        print("backward")

        # browser forward
        driver.forward()

        print("forward")

        pageSource = driver.page_source

        driver.close()

        driver.quit()

ff = BrowserInteractions()

ff.test()
