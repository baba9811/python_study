"""
파일 : day15-03-web_crawling3
개요 : 웹 페이지 가져오기
page : 318 ~ 321
"""
import requests
'''
* requests - 웹 페이지의 모든 정보가 담겨 있는 소스 코드를 가져오기 위한 라이브러리 
* BeautifulSoup - 원하는 정보만 추출하기 위한 라이브러리 
'''

'''
1. 일반 웹 페이지 정보 가져오기
'''

# url = 'https://www.naver.com'
# response = requests.get(url)
# print(f'응답코드 {response.status_code}')
# with open('response.txt', mode='wt', encoding='utf-8') as file:
#     file.write(response.text)

'''
2. 검색 결과 웹 페이지 정보 가져오기
네이버에서 검색 후 URL을 자세하게 살펴보면 ?기준 오른쪽으로
파라미터명=값&파라미터명=값.... 같은 형식으로 데이터가 전달되는 것을 확인할 수 있다.

네이버에서는 query라는 파라미터를 이용하여 검색을 한다.

파라미터는 dict 타입으로 전송하면됩니다.
'''

# url = 'https://search.naver.com/search.naver'
# param = {'query': '코로나'}
# response = requests.get(url, params=param)
# print(response.text)

'''
책 예제 )
네이버 영화에서 2019년에 개봉한 봉준호 감독의 영화 '기생충'의 소개 페이지를
가져오는 프로그램입니다.
'''

url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param = {'code': 161967}
response = requests.get(url, params=param)
with open('response.txt', mode="wt", encoding='utf-8') as file:
    file.write(response.text)














