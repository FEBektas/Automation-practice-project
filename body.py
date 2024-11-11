from selenium import webdriver
from selenium.webdriver.common.by import By


# -----> The website url and chrome driver <-----
URL = "https://myanimelist.net/"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)

# -----> Solution 1 <----
# *tapping the disagree button for the cookie agent.
disagree_button = driver.find_element(By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
disagree_button.click()

# -----> Solution 2 <----
# *tapping the agree button for the cookie agent.

# agree_button = driver.find_element(By.CLASS_NAME, "css-47sehv")
# agree_button.click()

# -----> Body <-----
# -----> Finds all images on the website <-----
images = driver.find_elements(By.TAG_NAME, "img")

# -----> Returns all found images into number <-----
total_images = len(images)

# -----> Setting the counter for the missing sources to 0 <-----
missing_src = 0

# -----> All images that don't have the src attribute and finds them with another attribute "alt" <-----
for img in images:
    src = img.get_attribute("src")
    if not src:
        missing_src += 1
        image_name = img.get_attribute("alt")
        print(f"The following imagine {image_name} is missing the source attribute!")
print("\n")
# -----> Finding all broken links <-----
links = driver.find_elements(By.TAG_NAME, "a")
total_links = len(links)
missing_links = 0

# -----> Finding if the link has a href attribute <-----
for link in links:
    href = link.get_attribute("href")
    if not href:
        missing_links += 1
        print(f"The {link.text} button has no external link")


driver.quit()

print(f"\nIn total there are {total_images} many images on the {URL}, and {missing_src} are missing src attribute!\n")
print(f"In total there are {total_links} many with external and {missing_links} are not having external links!")
