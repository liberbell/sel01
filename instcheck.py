from hashlib import blake2b
from selenium import webdriver
from PIL import Image

browser = webdriver.Safari()
# browser = webdriver.Chrome()

browser.get("https://scraping-for-beginner.herokuapp.com/login_page")


elem_username = browser.find_element_by_id("username")
print(elem_username)
browser.quit()