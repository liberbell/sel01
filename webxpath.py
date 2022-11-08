from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
URL = "https://scraping-for-beginner.herokuapp.com/"
browser.get(URL)

# /html/body/div[2]/div/div/div[1]/ul/li[1]
xpath = "/html/body/div[2]/div/div/div[1]/ul/li[1]"
browser.find_element()