from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class FindByXpathCss():

    def test(self):

        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.get(baseUrl)
        elementByXpath = driver.find_element(By.XPATH, "//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByCss = driver.find_element(By.CSS_SELECTOR, "#displayed-text")

        if elementByCss is not None:
            print("we found an element by Css")


ff = FindByXpathCss()

ff.test()
