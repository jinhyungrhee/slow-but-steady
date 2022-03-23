'''
티비랭킹닷컴(https://workey.codeit.kr/ratings/index)사이트에서 제공되는 모든 데이터를 받아올 수 있도록
모든 페이지의 HTML코드(response의 text)를 가져와서 rating_pages에 저장!

2010년 1월부터 2012년 12월 까지 모든 달에 대해 1주차~5주차 페이지를 순서대로 리스트에 넣기
(모든 달에 5주차가 있다고 가정)
'''

import requests

# 코드를 작성하세요
rating_pages = []
for i in range(2010, 2013):
    for j in range(1, 13):
        for k in range(5):
            page = requests.get(f"https://workey.codeit.kr/ratings/index?year={i}&month={j}&weekIndex={k}")
            rating_pages.append(page.text)

# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드