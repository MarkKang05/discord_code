import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re

# page  = urllib.request.urlopen("http://ncov.mohw.go.kr/")
# text = page.read().decode("utf8")
# print(text)

html = requests.get('http://ncov.mohw.go.kr/')
#웹페이지 요청을 하는 코드이다. 특정 url을 적으면 웹피이지에 대한 소스코드들을 볼 수 있다.

#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
# data1 = soup.find('div', {'class':'wrap nj'})
# del soup
# data2 = data1.find('div', {'class':'mainlive_container'})
# del data1
# data3 = data2.find('div', {'class':'container'})
# del data2
# data4 = data3.find('div', {'class':'liveboard_layout'})
# del data3
# data5 = data4.find('div', {'class':'liveNumOuter'})
# del data4
# data6 = data5.find('div', {'class':'liveNum'})
# del data5
# data7 = data6.find('div', {'class':'liveNum'})
# del data6
cor = soup.find('span',{'class': 'before'}).text
del soup
cor = re.findall("\d+",cor)
print(cor[0])