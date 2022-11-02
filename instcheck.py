from hashlib import blake2b
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import pandas as pd

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
# hobby = elem_h.text.replace("\n", ",")
# print(elem_n.text, elem_c.text, elem_b.text, elem_f.text, hobby)
# # browser.quit()

elem_th = browser.find_element(By.TAG_NAME, value="th")
# print(elem_th.text)

elems_th = browser.find_elements(By.TAG_NAME, value="th")
# print(elems_th[0].text)
# print(len(elems_th))

keys = []
for  elem in elems_th:
    # print(elem.text)
    key = elem.text
    keys.append(key)

print(keys)

elems_td = browser.find_elements(By.TAG_NAME, value="td")

values = []
for elem in elems_td:
    value = elem.text
    values.append(value)

print(values)

df = pd.DataFrame()
df['Title'] = keys
df["Value"] = values
# print(df)

df.to_csv("trainer.csv", index=False)