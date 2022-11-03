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

elem_ranking1 = elem_rankingbox1.find_element(By.CLASS_NAME, value="u_rankBox")
# elem_ranking1 = int(elem_ranking1.text)
# print(type(elem_ranking1.text))

elem_fun1 = elem_ranking1.find_element(By.CLASS_NAME, value="u_categoryTipsItem")

rank1.append(title1.split("\n")[1])
rank1.append(elem_ranking1.text)

print(rank1)
browser.quit()