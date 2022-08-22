from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class FindByIdName():

    def test(self):

        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.get(baseUrl)
        elementById=driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element(By.NAME,"show-hide")

        if elementByName is not None:
            print("we found an element by Name")


ff = FindByIdName()

ff.test()
