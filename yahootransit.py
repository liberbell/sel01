# https://transit.yahoo.co.jp/search/result?
# from=%E3%81%BF%E3%81%AA%E3%81%A8%E3%81%BF%E3%82%89%E3%81%84
# &to=%E6%A8%AA%E6%B5%9C
# &fromgid=
# &togid=
# &flatlon=
# &tlatlon=%2C%2C23368
# &via=
# &viacode=
# &y=2022
# &m=11
# &d=09
# &hh=08
# &m1=5&m2=0
# &type=1
# &ticket=ic
# &expkind=1
# &userpass=1
# &ws=3
# &s=0
# &al=1
# &shin=1
# &ex=1
# &hb=1
# &lb=1
# &sr=1

from selenium import webdriver

browser = webdriver.Chrome()
URL = "https://transit.yahoo.co.jp/search/result?from={}&to={}&fromgid=&togid=&flatlon=&tlatlon=%2C%2C23368&via=&viacode=&y=2022&m=11&d=09&hh=08&m1=5&m2=0&type=1&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1".format("東京", "武蔵小杉")

elem = browser.get(URL)
