from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")