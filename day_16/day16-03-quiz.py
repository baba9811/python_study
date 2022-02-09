import wordcloud
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib
import random
"""
파일명 : day16-03-quiz
개요 : 응용문제
page : 348 ~ 349
"""

'''
1. 다음은 어떤 시리얼에 포함된 비타민의 함량을 나타낸 데이터입니다.
각 항목의 비율이 나타날 수 있도록 그래프로 표시하세요.

[ 데이터 ]
종류      |     함량
비타민A         0.18
비타민B1        0.3
비타민B2        3.33
니이아신         3.75
비타민B6        0.38
비타민C         25
비타민D         0.25
비타민E         2.75
엽산           0.1
'''

vitamins = {
    '비타민A': 0.18,
    '비타민B1': 0.3,
    '비타민B2': 3.33,
    '니이아신': 3.75,
    '비타민B6': 0.38,
    '비타민C': 25,
    '비타민D': 0.25,
    '비타민E': 2.75,
    '엽산': 0.1
}
# 라벨 []
vitaminsLabel = [vitamin for vitamin in vitamins]
# 값 []
vitaminsValue = [vitamins[key] for key in vitamins.keys()]
figure = plt.figure()
axes = figure.add_subplot(111)
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)
axes.pie(vitaminsValue, labels=vitaminsLabel, autopct='%0.1f%%')
plt.axis('equal')
plt.show()

'''
2. 다음 지시사항에 따라 랜덤 데이터를 생성한 뒤 그래프를 작성하세요.

[ 지시사항 ]
- 총 2개의 데이터를 생성합니다.
- 2개의 데이터 모두 x축과 y축의 범위는 0부터 100까지 입니다.
- 하나의 subplot에 꺽은선 그래프와 막대그래프를 동시에 배치합니다.
- 꺽은선 그래프에는 빨간색에 · ( ㄱ + 한자 + 2번째 8번) 모양의 marker를 적용하세요.
- 막대그래프에는 녹색으로 적용하세요
'''

# y => [0.. 100] ( 랜덤 )
plotX = list(range(0, 101))
plotY = list(range(0, 101))
random.shuffle(plotY)
barX = list(range(0, 101))
barY = list(range(0, 101))
random.shuffle(barY)
figure2 = plt.figure()
axes2 = figure2.add_subplot(111)
axes2.plot(plotX, plotY, marker='.', color='r')
axes2.bar(barX, barY, color='green')
plt.show()





