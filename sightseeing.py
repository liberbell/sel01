from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")

#body > div.row > div > div:nth-child(3)
# <div class="u_areaListRankingBox row">
#       <div class="u_title col s12">
#         <p></p><h2><span class="badge">1</span>観光地 1</h2><p></p>
#       </div>
#       <!-- 観光地イメージ -->
#       <div class="place_img col s12">
#         <img src="/static/assets/img/img1.JPG" alt="">
#       </div>
#       <!-- 総合評価 -->
#       <div class="u_rankBox col s12">
#         <span style="--rate: 94.0%;"></span><span class="evaluateNumber">4.7</span><br>
#       </div>
#       <!-- 各カテゴリ評価 -->
#       <div class="u_categoryTipsItem col s12">
#         <dl>
#           <dt>楽しさ</dt>
#           <dd class="is_rank"><span class="evaluateNumber">4.6</span></dd>
#           <dd class="comment">満喫できた</dd>
#         </dl>
#         <dl>
#           <dt>人混みの多さ</dt>
#           <dd class="is_rank"><span class="evaluateNumber">4.5</span></dd>
#           <dd class="comment">まぁまぁ混んでいた</dd>
#         </dl>
#         <dl>
#           <dt>景色</dt>
#           <dd class="is_rank"><span class="evaluateNumber">4.9</span></dd>
#           <dd class="comment">大自然を感じることができた</dd>
#         </dl>
#         <dl>
#           <dt>アクセス</dt>
#           <dd class="is_rank"><span class="evaluateNumber">4.2</span></dd>
#           <dd class="comment">飛行機で1時間ほどで着きました</dd>
#         </dl>
#       </div>
#       <div class="divider">
#       </div>
#     </div>
rank1 = []
elem_rankingbox1 = browser.find_element(By.CLASS_NAME, value="u_areaListRankingBox")
elem_title1 = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_title").find_element(By.TAG_NAME, value="h2")

title1 = elem_title1.text

elem_ranking1 = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_rankBox").find_element(By.CLASS_NAME, value="evaluateNumber")
# elem_ranking1 = int(elem_ranking1.text)
# print(type(elem_ranking1.text))

elem_rank1_func = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[0]
elem_rank1_crowd = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[1]
elem_rank1_view = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[2]
elem_rank1_access = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[3]

rank1.append(title1.split("\n")[1])
rank1.append(elem_ranking1.text)
rank1.append(elem_rank1_func.text)
rank1.append(elem_rank1_crowd.text)
rank1.append(elem_rank1_view.text)
rank1.append(elem_rank1_access.text)

# print(rank1)
# browser.quit()

rank2 =[]
elem_rankingbox2 = browser.find_elements(By.CLASS_NAME, value="u_areaListRankingBox")[1]
elem_title2 = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_title").find_element(By.TAG_NAME, value="h2")
title2 = elem_title2.text

elem_ranking2 = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_rankBox").find_element(By.CLASS_NAME, value="evaluateNumber")
elem_rank2_func = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[0]
elem_rank2_crowd = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[1]
elem_rank2_view = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[2]
elem_rank2_access = elem_rankingbox2.find_element(By.CLASS_NAME, value="u_categoryTipsItem").find_elements(By.CLASS_NAME, value="is_rank")[3]

rank2.append(title2.split("\n")[1])
rank2.append(elem_ranking2.text)
rank2.append(elem_rank2_func.text)
rank2.append(elem_rank2_crowd.text)
rank2.append(elem_rank2_view.text)
rank2.append(elem_rank2_access.text)

# print(rank2)

titles = []
ranks = []
i = 0
elem_sites = browser.find_elements(By.CLASS_NAME, value="u_areaListRankingBox")
for elem_site in elem_sites:
    elem_title = elem_site.find_element(By.CLASS_NAME, value="u_title")
    title = elem_title.text.split("\n")[1]
    titles.append(title)
    # i +=1ß

elems_ranks = browser.find_elements(By.CLASS_NAME, value="u_rankBox")
for elem_rankbox in elems_ranks:
    elem_rank = elem_rankbox.find_element(By.CLASS_NAME, value="evaluateNumber")
    # print(elem_rank.text)
    rank = float(elem_rank.text)
    ranks.append(rank)
# print(elems_rank)

elem_categoryitems = []
_ranks = []
elems_tipsitems = browser.find_elements(By.CLASS_NAME, value="u_categoryTipsItem")

for elem_tipsitem in elems_tipsitems:
    elem_categoryitems = elem_tipsitem.find_elements(By.CLASS_NAME, value="is_rank")
    # print(len(elem_categoryitems))
    for elem_categoryitem in elem_categoryitems:
        elem_categoryrank = elem_categoryitem.find_elements(By.CLASS_NAME, value="evaluateNumber").text
        _ranks.append(elem_categoryrank)
    

print(titles)
print(ranks)
print(_ranks)