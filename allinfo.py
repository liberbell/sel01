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

    elems_ranks = browser.find_elements(By.CLASS_NAME, value="u_rankBox")
    for elem_rankbox in elems_ranks:
        elem_rank = elem_rankbox.find_element(By.CLASS_NAME, value="evaluateNumber")
        rank = float(elem_rank.text)
        ranks.append(rank)

    elem_tipsitems = browser.find_elements(By.CLASS_NAME, value="u_categoryTipsItem")
    for elem_tipsitem in elem_tipsitems:
        elem_categoryitems = elem_tipsitem.find_elements(By.CLASS_NAME, value="is_rank")
        _ranks = []
        for elem_categoryrank in elem_categoryitems:
            elem_rank = elem_categoryrank.find_element(By.CLASS_NAME, value="evaluateNumber").text
            _ranks.append(elem_rank)
        categories.append(_ranks)

print(title)
print(ranks)
print(categories)

df = pd.DataFrame()

df["Site"] = titles
df["ranks"] = ranks
df_categories = pd.DataFrame(categories)
df_categories.columns = ["fun", "crowded", "view", "access"]