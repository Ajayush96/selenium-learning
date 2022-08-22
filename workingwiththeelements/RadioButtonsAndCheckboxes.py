from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service


class RadioButtonsAndCheckboxes():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element(By.XPATH, "//input[@id='benzradio']")
        benzRadioBtn.click()

        time.sleep(2)

        hondaRadioBtn = driver.find_element(By.XPATH, "//input[@id='hondaradio']")
        hondaRadioBtn.click()

        time.sleep(2)

        bmwCheckBox = driver.find_element(By.XPATH, "//input[@id='bmwcheck']")
        bmwCheckBox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element(By.XPATH, "//input[@id='benzcheck']")
        benzCheckbox.click()

        time.sleep(2)

        hondaCheckbox = driver.find_element(By.XPATH, "//input[@id='hondacheck']")
        hondaCheckbox.click()

        time.sleep(2)

        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected()))  # throw true is selected else false
        print("Benz radio button is selected?" + str(benzRadioBtn.is_selected()))
        print("Honda radio button is selected?" + str(hondaRadioBtn.is_selected()))

        print("BMW checkbox button is selected? " + str(bmwCheckBox.is_selected()))  # throw true is selected else false
        print("Benz checkbox button is selected?" + str(benzCheckbox.is_selected()))
        print("Honda checkbox button is selected?" + str(hondaCheckbox.is_selected()))


ff = RadioButtonsAndCheckboxes()
ff.test()
