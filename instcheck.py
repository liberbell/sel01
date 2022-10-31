from selenium import webdriver
from PIL import Image

browser = webdriver.Safari()
# browser = webdriver.Chrome()

browser.get("https://scraping-for-beginner.herokuapp.com/login_page")