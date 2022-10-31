from hashlib import blake2b
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
# browser = webdriver.Chrome()

browser.get("https://scraping-for-beginner.herokuapp.com/login_page")


elem_username = browser.find_element(By.ID, value="username")
print(elem_username)
elem_username.send_keys("imanishi")
# browser.quit()