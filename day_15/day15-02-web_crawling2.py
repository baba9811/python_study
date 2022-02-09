"""
파일명 : web_crawling2
개요 : 웹 크롤링의 이해
page : 315 ~ 317
"""

'''
웹 크롤링이란 완성된 웹 페이지에서 필요한 정보를 수집하고 선별하여 추출하는 과정을 의미합니다.
다른 말로 웹 스크래핑이라고 합니다.
방대한 웹의 자료를 가져와서 가공하려면 웹의 기초 지식인 HTML에 대해서 알고있어야합니다.
'''

'''
1. HTML의 개념
HTML은 Hyper Text Markup Language의 약자로 "웹 페이지를 만드는 문법을 갖춘 언어"
정도로 해석하면 된다.
HTML은 각자 역할이 정해진 태그(tag)들로 구성되어 있는데 그 태그들의 개수가 많지 않아
며칠만 공부해도 전반적인 내용을 살펴볼 수 있습니다. 

기본적으로 웹 페이지들은 '소스 보기'를 통해서 어떤 HTML 태그들로 만들었는지 
확인 할 수 있습니다.

HTML 문서는 상위 요소와 하위 요소가 존재하는 트리 구조(계층 구조)입니다.

<!DOCTYPE html> -> HTML5 임을 브라우저에게 알리는 선언문
이후 html 태그부터 실제 HTML 태그 요소

<html> </html> 사이에 작성되며
<head>, <body> 태그가 <html> 하위 태그에 있습니다. 
<html>
    <head></head>
    <body></body>
</html>

[ HTML 요소의 구조 예시]
<div class="container">HTML</div>
<div> - 시작 태그
div - 태그 종류
class - 속성 이름
"container" - 속성 값 
HTML - 내용
</div> - 종료 태그 
'''

'''
3. URL
URL이란 Uniform Resource Locator의 약자로 어떤 자원의 위치를 표기하는 방법을 의미합니다.
구글에 접속하고 싶을때 https://www.google.com <- 주소 입력 
URL 입력 

[ 형식 ] 
프로토콜://도메인:포트/경로
* 포트 80은 생략됨
'''




















