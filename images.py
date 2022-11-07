from PIL import Image
from selenium import webdriver

# img = Image.open("aircraft.jpg")
# img.show()

# img = img.resize((1024, 768))
# img.show()
# print(img.size)
# img.save("sample_resize.jpg")

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/image")