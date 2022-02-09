import wordcloud
import matplotlib.pyplot as plt
"""
개요 : wordcloud
page : 346 ~ 347
"""

'''
1. wordcloud 설치하기
wordcloud 라이브러리 역시 외부 라이브러리이기 때문에 설치해야 사용할 수 있습니다.
[ 원하는 파이썬 설치 ]
-> 원하는 파이썬 설치 경로/Scripts 이동
-> cmd ( 명령 프롬프트 )를 실행
-> pip install wordcloud 입력 후 엔터 
'''

'''
2. wordcloud 생성하기
wordcloud 라이브러리는 matplotlib 라이브러리와 함께 사용합니다.
가장 먼저 wordcloud 모듈로 워드클라우드를 생성한 뒤
생성된 워드클라우드를 matplotlib 라이브러리로 출력합니다. 
'''

words = {
    'Python': 10,
    'Java': 5,
    'C': 7,
    'C++': 9,
    'JSP': 12
}

# wc = wordcloud.WordCloud()
# cloud = wc.generate_from_frequencies(words)
# plt.figure()
# plt.imshow(cloud)
# plt.show()

'''
한글을 이용해서 wordcloud를 생성하려면 추가 작업이 필요합니다.
-> 글꼴을 한글 폰트로 변경
'''

words = {
    '파이썬': 20,
    '빅데이터': 5,
    '웹크롤링': 7,
    '인공지능': 9,
    '딥러닝': 12
}

# wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/malgun.ttf')
# cloud = wc.generate_from_frequencies(words)
# plt.figure()
# plt.imshow(cloud)
# plt.show()

'''
# wordcloud 공식 홈페이지
https://amueller.github.io/word_cloud/index.html
'''

"""
깜짝 퀴즈 )
단어를 20번 입력받아서 그 단어들로 wordcloud를 만들어보자.
( 이미 입력단어는 크기가 커진다 )
"""

words = {}

# for i in range(20):
#     word = input('단어를 입력하세요 >>>')
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1
#
# wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/malgun.ttf')
# cloud = wc.generate_from_frequencies(words)
# plt.figure()
# plt.imshow(cloud)
# plt.show()

import random

def ran():
    return random.randint(1, 1000)

words = {
    'ㅂ': ran(),
    'ㅈ': ran(),
    'ㄷ': ran(),
    'ㄱ': ran(),
    'ㅅ': ran(),
    'ㅁ': ran(),
    'ㄴ': ran(),
    'ㅇ': ran(),
    'ㅎ': ran(),
    'ㅋ': ran(),
    'ㅌ': ran(),
    'ㅊ': ran(),
    'ㅍ': ran(),
    'ㅠ': ran()
}

wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/malgun.ttf')
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()