from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Chrome()

titles = []
ranks = []
categories = []

for page in range(1, 4):
    
    browser.get("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(page))
    
    elem_sites = browser.find_elements(By.CLASS_NAME, value="u_areaListRankingBox")
    for elem_site in elem_sites:
        elem_title = elem_site.find_element(By.CLASS_NAME, value="u_title")
        title = elem_title.text.split("\n")[1]
        titles.append(title)