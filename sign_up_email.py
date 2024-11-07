import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# -----> The website url and chrome driver <-----
URL = "https://myanimelist.net/"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# -----> Credentials <-----
email = "test1@gmail.com"
username = "tester1"
password = "tester1"

# -----> lists with random selections <-----
month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month = random.choice(month_list)
# print(month)
day = random.randint(1, 31)
year = random.randint(1930, 2025)

# print(month, day, year)

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


# -----> Finding the Sign-up button <-----
sign_up = driver.find_element(By.CLASS_NAME, "btn-signup")
sign_up.click()

time.sleep(2)

# ----> Finding the Input Fields <-----
email_field = driver.find_element(By.ID, "loginEmail")
user_name_field = driver.find_element(By.NAME, "user_name")
password_field = driver.find_element(By.ID, "password")
month_dropdown = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/form/div[1]/fieldset/div/select[1]")
day_dropdown = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/form/div[1]/fieldset/div/select[2]")
year_dropdown = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/form/div[1]/fieldset/div/select[3]")


# -----> Completing the search fields <-----
email_field.send_keys(f"{email}")
user_name_field.send_keys(f"{username}")
password_field.send_keys(f"{password}")
month_dropdown.send_keys(f"{month}")
time.sleep(1)
day_dropdown.send_keys(f"{day}")
time.sleep(1)
year_dropdown.send_keys(f"{year}")
time.sleep(1)

time.sleep(3)
driver.quit()
