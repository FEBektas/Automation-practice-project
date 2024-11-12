import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# -----> The website url and chrome driver <-----
URL = "https://myanimelist.net/"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
actions = ActionChains(driver)

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

# -----> Home Button <-----
home_button = driver.find_element(By.CLASS_NAME, "link-mal-logo")


# -----> funct to check the href attribute for the drop-down menu <-----
def statement():
    element = driver.find_element(By.XPATH, f"//*[@id='nav']/li[{x}]/ul/li[{r}]/a")
    href = element.get_attribute("href")
    print(f"The -- {element.text} --- has the following link: {href}")


# -----> for loop for printing the name and the href link for every item in the drop-down <-----
for x in range(1, 8):
    nav_bar = driver.find_element(By.XPATH, f"//*[@id='nav']/li[{x}]/a")
    nav_bar.click()
    print(f"\nThe current section is: {nav_bar.text}")
    for r in range(1, 9):
        if nav_bar.text == "Anime":
            statement()
        if nav_bar.text == "Manga" and r < 7:
            statement()
        if nav_bar.text == "Community" and r < 6:
            statement()
        if nav_bar.text == "Industry" and r < 7:
            statement()
        if nav_bar.text == "Watch" and r < 3:
            statement()
        if nav_bar.text == "Read" and r < 2:
            statement()
        if nav_bar.text == "Help" and r < 8:
            statement()
        else:
            pass
time.sleep(1)

# -----> Filter drop down (Right section of the header) <-----
top_search_value = driver.find_element(By.ID, "topSearchValue")
top_search_value.click()

# -----> Finds the filter drop down element by ID and scrolls down at the bottom,
# after scrolling it will click on the first element "All"
for r in range(1, 13):
    top_search_value.send_keys(Keys.ARROW_DOWN)
top_search_value.click()
driver.find_element(By.XPATH, "//*[@id='topSearchValue']/option[1]").click()

# -----> Search field (Right side of the header.) <-----
search_field = driver.find_element(By.ID, "topSearchText")
# "text" variable was created as an example, but you can use any string.
text = "Kaguya"

# Using the actions library we are performing the following actions:
# 1. Moving into the search field.
actions.move_to_element(search_field)
# 2. Clicking on the search field.
actions.click(search_field).perform()
time.sleep(1)
# 3. Sending whatever text we want into the search field.
actions.send_keys(text).perform()
time.sleep(2)
# searching for the "text" entered above.
driver.find_element(By.ID, "topSearchButon").click()

# -----> Returning to the front page by clicking on the Home Button <-----
home_button = driver.find_element(By.XPATH, "//*[@id='headerSmall']/a")
home_button.click()


# -----> Header sign-up <-----
# Finding the elements.
external_signup = driver.find_element(By.XPATH, "//*[@id='myanimelist']/div[2]/div[3]/div[3]/div[1]/div")

# -----> Forloop to search the href for every sign-up button <-----
for r in range(1, 5):
    header_signup = driver.find_element(By.XPATH, f"//*[@id='myanimelist']/div[2]/div[3]/div[3]/div[1]/div/a[{r}]")
    href1 = header_signup.get_attribute("href")
    print(f"The -- {header_signup.text} -- has an external link: {href1}")

# -----> Header sign-up by Email <-----
mail_signup = driver.find_element(By.XPATH, "//*[@id='myanimelist']/div[2]/div[3]/div[3]/div[2]/a")
href2 = mail_signup.get_attribute("href")
print(f"\nThe -- {mail_signup.text} -- has the following link: {href2}")

time.sleep(2)
driver.quit()
