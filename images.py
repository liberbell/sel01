from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

# img = Image.open("aircraft.jpg")
# img.show()

# img = img.resize((1024, 768))
# img.show()
# print(img.size)
# img.save("sample_resize.jpg")

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/image")
# <div class="material-placeholder" style=""><img class="materialbox responsive-img card" src="/static/assets/img/img1.JPG" style=""></div>

elem = browser.find_element(By.CLASS_NAME, value="material-placeholder")
elem = elem.find_element(By.CLASS_NAME, value="src")