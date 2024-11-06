import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys


# -----> The website url and chrome driver <-----

URL = "https://myanimelist.net/#:~:text=Anime%20rec%20by%20erikkamirs%20-%205%20hours%20ago.%20Welcome%20to"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# -----> Finding elements <-----

# -----> Solution 1 <----
# *tapping the agree button for the cookie agent.

# agree_button = driver.find_element(By.CLASS_NAME, "css-47sehv")
# agree_button.click()


# -----> Solution 2 <-----
# *tapping the disagree button for the cookie agent.
disagree_button = driver.find_element(By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
disagree_button.click()

# -----> Finding the sign-up button and clicking on it <-----
sign_up = driver.find_element(By.CLASS_NAME, "btn-signup")
sign_up.click()
# driver.fullscreen_window()

time.sleep(2)


# -----> Sing-up buttons <-----
google_button = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/div[2]/div/div[1]/a[1]")
apple_button = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/div[2]/div/div[1]/a[2]")
facebook_button = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/div[2]/div/div[2]/a[1]")
twitter_button = driver.find_element(By.XPATH, "//*[@id='dialog']/tbody/tr/td/div[2]/div/div[2]/a[2]")

# -----> External button list <-----

elements = [google_button, apple_button, facebook_button, twitter_button]

# -----> Loop to check for href for the external link buttons <------
# The loop is looking for the href attribute in the external sign-up buttons.
for element in elements:
    href = element.get_attribute("href")
    if href:
        print(f"The {element.text} button has external link: {href}")
    else:
        print(f"The {element.text} button does not have external link")


time.sleep(2)
driver.quit()
