import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class AutoComplete():

    def test(self):
        baseUrl = "https://www.goibibo.com"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        partialText = "Dar"
        textToSelect = "Darbhanga, India(DBR)"  # this thing should be matched

        textElement = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/input")
        textElement.send_keys(partialText)

        ulElement = driver.find_element(By.ID,"autoSuggest-list")
        inner_html = ulElement.get_attribute("innerHTML")
        print(inner_html)

        liElements= ulElement.find_elements(By.TAG_NAME, "li")
        time.sleep(2)

        for element in liElements:

            #print(element.text)
            if textToSelect in element.text:
                element.click()
                break
        time.sleep(4)



        driver.quit()


ff=AutoComplete()

ff.test()

