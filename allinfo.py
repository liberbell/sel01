from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Chrome()


titles = []
ranks = []
categories = []

for page in range(1, 4):
    browser.get("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(page))