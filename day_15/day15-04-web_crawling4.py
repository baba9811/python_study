"""
파일명 : day15-04-web_crawling4
개요 : 웹 페이지 분석 및 추출하기
page : 322 ~ 325
"""

'''
* 지금까지는 requests를 통해서 웹 페이지의 소스만 가져오는 작업을 했습니다.
이제는 가져온 웹페이지 소스를 BeautifulSoup를 이용해서 원하는 정보를 추출해보겠습니다.
'''

'''
1. BeautifulSoup 객체 생성하기
requests를 사용해서 가져온 웹 페이지는 BeautifulSoup() 함수와 html 파서를 이용해서
쉽게 해석이 가능한 BeautifulSoup 객체로 변경한 뒤 데이터를 추출
[ 형식 ]
import requests
from bs4 import BeautifulSoup

url = '검색 대상 URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

'''
2. BeautifulSoup 메소드 사용하기
대표적인 메소드를 사용해보겠습니다.
- find() 메소드
-> 지정된 태그들 중에서 가장 첫번째 태그만 가져오는 메소드입니다.
일반적으로 하나의 태그만 존재하는 경우에 사용합니다.
'''

# <a href="" />
# print(soup.find('a'))
# print(soup.find('a').text)
# print(soup.find('a').get('href'))

'''
3. find_all() 메소드
지정한 태그들을 모두 가져오는 메소드입니다.
가져온 태그들은 모두 리스트에 보관합니다.
'''

# print(soup.find_all('a'))

'''
4. class 속성 활용하기
공통적인 특징을 갖는 태그들은 같은 class 속성값을 가지고있습니다.
크롤링에서 자주 사용되는 속성이기 때문에 특정 class 속성값을 찾는 방법이 따로 있습니다.
find() 메소드와 find_all() 메소드 모두 동일하게 지원합니다.
'''

#print(soup.find_all(class_="login_msg"))

'''
5. id 속성 활용하기
같은 웹 페이지에서 같은 id 속성값을 가진 태그는 존재하지 않습니다.
=> 유니크함 => 오직 하나만 가지고있다.
'''

#print(soup.find(id="u_skip"))

'''
6. 요소의 태그 구성 알아내기
크롬을 기준으로, 특정 요소의 태그 구성을 알아내는 방법은
크롬의 개발자 도구를 이용하는 것입니다.
개발자 도구는 f12를 누르면 실행되며 개발자 도구가 실행되면
코드 인스펙트 버튼을 클릭한 뒤 원하는 요소를 클릭해서 소스 코드를 알아낼 수 있습니다.
'''
# a = soup.find(class_="link_news")
# print(f'{a.text} - {a.get("href")}')
#
# url2 = a.get('href')
# res2 = requests.get(url)
# soup2 = BeautifulSoup(res2.text, 'html.parser')

'''
책 예제 )
1990년에 개봉한 크리스 콜럼버스 감독의 영화 '나홀로 집에'를 
네이버 영화에서 검색하면 5개의 한줄 평이 있습니다.
이 5개의 한줄평을 가져와서 출력하는 프로그램을 만들어봅시다.
'''

url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param = {'code':10016}
response = requests.get(url, params=param)
soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div', class_="score_reple")
for div in divs:
    print(div.find('p').text.strip())




