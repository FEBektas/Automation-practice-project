import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://myanimelist.net/"

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# -----> Bypassing the cookie agent <-----
# -----> If by any chance an error will be present at this line of code just re-run the test
# as sometimes the cookie agent will not be displayed. <-----

# -----> Solution 1 <----
# *tapping the disagree button for the cookie agent.
disagree_button = driver.find_element(By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
disagree_button.click()
time.sleep(1)

# -----> Solution 2 <----
# *tapping the agree button for the cookie agent.

# agree_button = driver.find_element(By.CLASS_NAME, "css-47sehv")
# agree_button.click()


# -----> dismissing the gdpr agent <-----

cookie_agent = driver.find_element(By.XPATH, "//*[@id='gdpr-modal-bottom']/div/div/div[2]/button")
cookie_agent.click()


# -----> Scrolling at the bottom of the page <-----
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.END)

time.sleep(1)

# -----> Finding the footer elements by href in the "Top Anime section"<-----

print("The current section is: Top Anime ")
for r in range(1, 6):
    top_anime_links = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[1]/ol/li[{r}]")
    element = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[1]/ol/li[{r}]/a")
    top_anime_href = element.get_attribute("href")
    print(f"The anime is {top_anime_links.text} and the external links is {top_anime_href}")

print("----------")

# -----> Finding the footer elements by href in the "Top Airing Anime section"<-----

print("The current section is: Top Airing Anime ")
for x in range(1, 6):
    top_air_anime = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[2]/ol/li[{x}]")
    elements2 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[2]/ol/li[{x}]/a")
    top_air_anime_href = elements2.get_attribute("href")
    print(f"The anime is {top_air_anime.text} and the external link is {top_air_anime_href}")

print("----------")

# -----> Finding the footer elements by href in the "Most Popular Characters"<-----

print("The current section is: Most Popular Characters ")
for y in range(1, 6):
    most_popular_ch = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[3]/ol/li[{y}]")
    elements3 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div[3]/ol/li[{y}]/a")
    most_popular_ch_href = elements3.get_attribute("href")
    print(f"The anime is {most_popular_ch.text} and the external link is {most_popular_ch_href}")

print("----------")

# -----> Finding the external links for all elements in the Footer <-----

# -----> The external links for the following footer sections: <-----
# -----> "Follow us" section <-----
for x in range(1, 3):
    footer_apps = driver.find_element(By.XPATH, f"//*[@id='footer-block']/div[1]/div[2]/a[{x}]")
    href_apps = footer_apps.get_attribute("href")
    text_link1 = str(href_apps)
    # transforms the href link into a string and then splits the text by the dot and next print the second element in the list.
    print(f"The {text_link1.split(".")[1].capitalize()} buttons from the 'Get the App' has an external link: {href_apps}")

print("----------")

# -----> And "Get the app" section <-----
for r in range(1, 5):
    footer = driver.find_element(By.XPATH, f"//*[@id='footer-block']/div[1]/div[1]/a[{r}]")
    footer_href = footer.get_attribute('href')
    text_link = str(footer_href).split(".")
    # print(text_link)
    if len(text_link) == 3:
        # transforms the href link into a string and then splits the text by the dot and next print the second element in the list.
        print(f"The following {text_link[1].capitalize()} social media from the 'Follow Us' section have an external link: {footer_href}")
    else:
        # transforms the href link into a string and then splits the text by the dot and next print the first element in the list,
        # and after that slices the first 8 characters to print only the intended string.
        print(f"The following {text_link[0][8:].capitalize()} social media from the 'Follow Us' section have an external link: {footer_href}")


print("----------")

# -----> "Home" Footer <-----
home_footer = driver.find_element(By.XPATH, "//*[@id='footer-block']/div[2]/p[1]/a")
home_href = home_footer.get_attribute("href")
print(f"The footer section is {home_footer.text} and has an external link: {home_href}")

print("----------")

# -----> Footer external links <-----
for r in range(1, 13):
    time.sleep(1)
    footer_elements = driver.find_element(By.XPATH, f"//*[@id='footer-block']/div[2]/p[2]/a[{r}]")
    if r == 9:
        continue
    elements_href = footer_elements.get_attribute("href")
    print(f"The following sections are {footer_elements.text} and they all have an external link: {elements_href}")


print("----------")

# -----> Footer connection links <-----
login_footer = driver.find_element(By.XPATH, "//*[@id='malLogin']")
login_href = login_footer.get_attribute("href")
print(f"The footer {login_footer.text} element has an external link: {login_href}")

signup_footer = driver.find_element(By.XPATH, "//*[@id='footer-block']/div[2]/p[3]/a[2]")
signup_href = signup_footer.get_attribute("href")
print(f"The footer {signup_footer.text} element has an external link: {signup_href}")

print("----------")

# -----> "Recommended footer section <-----
for r in range(1, 4):
    recommended = driver.find_element(By.XPATH, f"//*[@id='footer-block']/div[3]/div/a[{r}]")
    recommended_href = recommended.get_attribute("href")
    print(f"The following elements {recommended.text} have the following external links: {recommended_href}")

driver.quit()
