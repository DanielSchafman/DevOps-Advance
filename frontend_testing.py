from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
driver = webdriver.Chrome(options=options)
user_id = 2

driver.get("http://127.0.0.1:5001/users/" + str(user_id))

print(driver.title)
sleep(5)