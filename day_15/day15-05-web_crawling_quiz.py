"""
파일명 : day15-05-web_crawling_quiz
개요 : 응용문제
page : 326 ~ 328
"""

import requests
from bs4 import BeautifulSoup

'''
1. 네이버 영화 사이트에 접속하면 영화랭킹 > 랭킹 > 영화인 메뉴를 통해서 
영화인 랭킹을 1위부터 50위까지 확인 할 수 있습니다.
이 전체 목록을 크롤링한 뒤 movie_in 리스트에 저장하세요.
확인을 위해 movie_in요소를 출력하세요.

[ 지시사항 ]
- 접속할 URL
https://movie.naver.com/movie/sdb/rank/rpeople.nhn
- 별도의 요청 파라미터는 없습니다.
'''

# url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# tds = soup.find_all('td', class_="title")
#
# movie_in = []
# for td in tds:
#     movie_in.append(td.text)
#
# print(movie_in)

'''
2. 네이버 영화 사이트에 접속하면 영화랭킹 > 랭킹 > 영화 메뉴를 통해서 영화 랭킹을 
조회순, 평점순(현재상영영화), 평점순(모든영화) 별로 1위부터 50위까지 확인할 수 있습니다.
이 중에서 조회순으로 전체 영화 제목을 크롤링한 뒤 movie 리스트에 저장하고 
movie 리스트의 전체 목록과 영화별 순위를 함께 출력하세요.

[ 지시사항 ]
- 접속할 URL은 다음과 같습니다.
https://movie.naver.com/movie/sdb/rank/rmovie.nhn
- 별도의 파라미터는 없습니다.

[ 출력 ]
1위 ..
2위 ..
3위 ..
'''

# url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# tds = soup.find_all('div', class_="tit3")
#
# movie = []
# for td in tds:
#     movie.append(td.text.strip())
#
# for i, m in enumerate(movie, start=1):
#     print(f'{i}위 {m}')

'''
3. 응용 문제 2에서 조회순 영화 랭킹 1위부터 50위까지 크롤링하였습니다.
이 중에서 순위가 상승한 영화의 제목만 크롤링하세요.

[ 지시 사항 ]
- 접속할 URL은 다음과 같습니다.
https://movie.naver.com/movie/sdb/rank/rmovie.nhn
'''

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
trs = soup.find_all('tr')
movie = []

for tr in trs:
    arrow = tr.find(class_="arrow")
    if arrow is not None:
        alt = arrow.get('alt')
        if alt.strip() == 'up':
            movie.append(tr.find(class_='tit3').text.strip())

print(movie)





