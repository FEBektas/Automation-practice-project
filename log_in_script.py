import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# -----> The website url and chrome driver <-----
URL = "https://myanimelist.net/"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# -----> Credentials <-----
# for the credentials to work you will need to set up your own environment.
email = os.getenv("username")
password = os.getenv("password")

# print(username)

# -----> Bypass the cookie agent <-----
# -----> If by any chance an error will be present at this line of code just re-run the test
# as sometimes the cookie agent will not be displayed. <-----

# -----> Solution 1 <----
# *tapping the disagree button for the cookie agent.
disagree_button = driver.find_element(By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
disagree_button.click()

# -----> Solution 2 <----
# *tapping the agree button for the cookie agent.

# agree_button = driver.find_element(By.CLASS_NAME, "css-47sehv")
# agree_button.click()

# -----> Finding the log in button <-----
login = driver.find_element(By.CLASS_NAME, "btn-login")
login.click()

# ----->  Finding the inputs for credentials <-----
username_field = driver.find_element(By.XPATH, "//*[@id='loginUserName']")
username_field.send_keys(f"{email}")
time.sleep(1)

password_field = driver.find_element(By.XPATH, "//*[@id='login-password']")
password_field.send_keys(f"{password}")
time.sleep(1)

login_button = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/form/div/p[6]/input")
login_button.send_keys(Keys.RETURN)
time.sleep(2)

time.sleep(2)
driver.quit()
