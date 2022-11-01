from hashlib import blake2b
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

# browser = webdriver.Safari()
# browser = webdriver.Chrome()

browser = webdriver.Chrome(executable_path='./chromedriver')

browser.get("https://scraping-for-beginner.herokuapp.com/login_page")


elem_username = browser.find_element(By.ID, value="username")
elem_username.send_keys("imanishi")

elem_password = browser.find_element(By.ID, value="password")
elem_password.send_keys("kohei")

elem_botton = browser.find_element(By.ID, value="login-btn")
elem_botton.click()

elem_n = browser.find_element(By.ID, value="name")
elem_c = browser.find_element(By.ID, value="company")
elem_b = browser.find_element(By.ID, value="birthday")
elem_f = browser.find_element(By.ID, value="come_from")
elem_h = browser.find_element(By.ID, value="hobby")
# print(type(elem_h.text))
hobby = elem_h.text.replace("\n", ",")
print(elem_n.text, elem_c.text, elem_b.text, elem_f.text, elem_h.text)
# browser.quit()