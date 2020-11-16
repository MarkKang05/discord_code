import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re

# page  = urllib.request.urlopen("http://ncov.mohw.go.kr/")
# text = page.read().decode("utf8")
# print(text)

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EC%8B%9C+%EB%82%A0%EC%94%A8')
#웹페이지 요청을 하는 코드이다. 특정 url을 적으면 웹피이지에 대한 소스코드들을 볼 수 있다.

#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

data1 = str(soup.find('ul', {'class':'list_area'}))


def span_to_span(data):
	#print(data)
	loc_list =[]
	temp1 = 0
	for i in range(92):
		temp1 = data.find('span',temp1+1)
		loc_list.append(temp1)
		print(temp1)
	
	
	for i in range(0,92-1):
		print(data[loc_list[i]:loc_list[i+1]])


span_to_span(data1)
