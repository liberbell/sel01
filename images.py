from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import io
from urllib import request
import os

# img = Image.open("aircraft.jpg")
# img.show()

# img = img.resize((1024, 768))
# img.show()
# print(img.size)
# img.save("sample_resize.jpg")

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/image")
# <div class="material-placeholder" style=""><img class="materialbox responsive-img card" src="/static/assets/img/img1.JPG" style=""></div>

URLs = []
# elem = browser.find_element(By.CLASS_NAME, value="material-placeholder")
# elem = elem.find_element(By.TAG_NAME, value="img")
# # print(elem.get_attribute("src"))
# URL = elem.get_attribute("src")

# f = io.BytesIO(request.urlopen(url=URL).read())
# img = Image.open(f)
# img.show()
# img.save("image01.jpg")

elems = browser.find_elements(By.CLASS_NAME, value="material-placeholder")
for elem in elems:
    img_tag = elem.find_element(By.TAG_NAME, value="img")
    url = img_tag.get_attribute("src")
    # print(url)
    URLs.append(url)
    # print(URLs)

for URL in URLs:
    f = io.BytesIO(request.urlopen(url=URL).read())
    sep_url = os.path.split(URL)
    print(sep_url[1])
    # img = Image.open(f)
    # img.show()