from hashlib import blake2b
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
# browser = webdriver.Chrome()

browser.get("https://scraping-for-beginner.herokuapp.com/login_page")


elem_username = browser.find_element(By.ID, value="username")
elem_username.send_keys("imanishi")

elem_password = browser.find_element(By.ID, value="password")
elem_password.send_keys("kohei")

elem_botton = browser.find_element(By.ID, value="login-btn")

# browser.quit()