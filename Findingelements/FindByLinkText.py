from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class FindByLinkText():

    def test(self):

        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.get(baseUrl)
        elementByLinkText = driver.find_element(By.LINK_TEXT, "Sign In")

        if elementByLinkText is not None:
            print("We found an element by LinkText")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "Pract")

        if elementByPartialLinkText is not None:
            print("we found an element by partialLinkText")


ff = FindByLinkText()

ff.test()
