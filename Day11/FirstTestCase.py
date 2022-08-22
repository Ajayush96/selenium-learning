# Test Case
# 1.Open the Chrome web  browser
# 2.open url
# 3.Enter username
# 4.Enter password
# 5.click login
# 6.capture title of the home page
# 7. verify title of the-page
# 8. close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/stinger/Downloads/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

act_title = driver.title

exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test pass")
else:
    print("login test fail")

driver.close()
