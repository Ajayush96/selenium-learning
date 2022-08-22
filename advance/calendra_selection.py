from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class CalendraSelection():

    def test1(self):
        baseUrl = "https://www.expedia.com"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # click flights tab
        driver.find_element(By.XPATH, "//span[contains(text(),'Flights')]").click()
        # find departing field
        departing_field = driver.find_element(By.ID, "d1-btn")
        departing_field.click()
        time.sleep(2)
        # find the date to be selected
        dateToSelect = driver.find_element(By.XPATH,
                                           "//div[@class='uitk-date-picker-month'][position()=1]//table[@class='uitk-date-picker-weeks']//tbody//tr[3]//button[@data-day='17']")
        dateToSelect.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click()
        time.sleep(5)

    def test2(self):
        baseUrl = "https://www.expedia.com"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # click flights tab
        driver.find_element(By.XPATH, "//span[contains(text(),'Flights')]").click()
        # find departing field
        departing_field = driver.find_element(By.ID, "d1-btn")
        departing_field.click()
        time.sleep(2)

        calMonth = driver.find_element(By.XPATH, "//div[@class='uitk-date-picker-month'][position()=1]")
        allValidates = calMonth.find_elements(By.TAG_NAME, "td")

        for date in allValidates:
            if date.find_element(By.XPATH, "//button[@data-day='17']").click():
                break


ff = CalendraSelection()
ff.test2()
