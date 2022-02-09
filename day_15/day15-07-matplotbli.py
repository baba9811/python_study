"""
파일명 : day15-07-matplotbli
개요 : batblib
page : 334 ~ 345
"""
import matplotlib.pyplot as plt

'''
1. matplotblib 설치
[ 원하는 파이썬 설치 ]
-> 원하는 파이썬 설치 경로/Scripts 이동
-> cmd ( 명령 프롬프트 ) 실행
-> pip install matplotlib 입력 후 엔터
'''

'''
2. figure와 subplot 
figure - subplot을 포함할 수 있는 전체 영역을 의미
subplot - 실제 그래프를 그리는 영역을 의미
=> 그래프가 그려진 공간을 subplot
=> 그 그래프들이 모여있는 전체 공간이 figure
'''

# figure = plt.figure()
# axes = figure.add_subplot(1, 1, 1) # 1행, 1열, 1번째 subplot
# plt.show()

# 행 - 가로 줄
# 열 - 세로 줄

# figure = plt.figure()
# axes1 = figure.add_subplot(1, 2, 1) # 1행 2열 1번째 subplot
# axes2 = figure.add_subplot(1, 2, 2) # 1행 2열 2번째 subplot
# plt.show()

'''
3. plot() 함수 
plot 함수는 꺽은선형그래프를 그리는 함수입니다.
plot(x, y)와 같이 x축에서 사용할 데이터와 y축에서 사용할 데이터를 각각 리스트로
만든 뒤 인수로 전달합니다.
'''

# axes = figure.add_subplot(111)
# x = [0, 1, 2, 3, 4]
# y = [4, 1, 2, 5, 2]
# axes.plot(x, y)
# plt.show()

'''
4개 옵션을 줄 수 있습니다.
linestyle - 선의 형태 [ 실선(solid), 대시(dashed), 점선(dotted) ]
linewidth - 선의 굵기 ( 포인트 단위의 실수 )
color - 선의 색상 
marker - 표식 
'''
# x = [0, 1, 2, 3, 4]
# y = [0, 3, 0, 3, 0]
# axes.plot(x, y, linestyle='dotted', linewidth=5.0)
# axes.plot(x, [1, 2, 3, 4, 5], color='r', marker='v')
# plt.show()

'''
4. 한글 처리
- 한글은 기본적으로 정상적으로 표시되지 않고 깨져서 표시된다.
이럴때 font-manager와 rc를 이용해서 사용하고자 하는 한글 폰트를 등록하면
이 문제를 해결할 수 있습니다.
'''

from matplotlib import font_manager
import matplotlib
# 사용하고자는 하는 폰트 선언
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)
plt.plot(['봄', '여름', '가을', '겨울'], [20.5, 30.5, 15.5, 1.5])
plt.show()

'''
책 예제 pass...
'''

'''
5. bar() 함수
막대그래프는 어떤 데이터의 많고 적음을 나타낼 때 주로 사용하고 파이썬에서는 
bar() 함수로 그릴 수 있습니다.
'''

figure = plt.figure()
axes = figure.add_subplot(111)
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [8, 6, 5, 4, 7, 9, 5]
axes.bar(x, y)
# 그래프에 제목 추가
plt.title('weekday call')
# 가로축에 제목 추가
plt.xlabel('week')
# 세로축에 제목 추가
plt.ylabel('call')
plt.show()

'''
6. scatter() 함수
산포 그래프 - 어떤 두 변수 사이의 상관관계를 나타낼 때 사용
'''

figure = plt.figure()
axes = figure.add_subplot(111)
x = [1, 2, 3, 4, 5, 6]
y = [6, 4, 1, 2, 7, 5]
area = [50, 100, 150, 200, 250, 300] # 각 점의 크기
color = ['red', 'green', 'blue', 'orange', 'aqua', 'crimson']
axes.scatter(x, y, s=area, c=color)
plt.show()

'''
책예제) 어느 집단의 소음에 따른 스트레스 지수를 조사하였더니 다음과 같은 결과가
나타났다고 가정합니다.
소음과 스트레스 지수의 상관관계를 시각적으로 표션하기 위해서 산포그래프를 그리는 프로그램입니다.
'''
d = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
s = [10, 11, 15, 20, 30, 42, 55, 70, 88, 110, 150]

figure = plt.figure()
axes = figure.add_subplot(111)
axes.scatter(d, s, s=50)
plt.xlabel('noise')
plt.ylabel('stress')
plt.show()