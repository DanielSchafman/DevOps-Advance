from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
driver = webdriver.Chrome(options=options)
user_id = 1

driver.get("http://127.0.0.1:5001/users/" + str(user_id))

user = driver.find_element(By.ID, "user").text
print(user)
driver.quit()