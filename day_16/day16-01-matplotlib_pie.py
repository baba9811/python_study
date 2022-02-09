"""
파일명 : day16-01-matplotlib_pie
page : 344 ~ 345
"""
import matplotlib.pyplot as plt

'''
1. pie() 함수
- 원형그래프는 전체에 대한 각 항목의 비율을 나타내고자 할 때 사용하는 것
'''

figure = plt.figure()
axes = figure.add_subplot(111)
data = [1, 2, 3]
axes.pie(data)
plt.axis('equal')
plt.show()

'''
pie() 함수를 이용해서 원형그래프를 만들 수 있습니다.
형태가 타원이 아닌 일반 원의 형태로 출력될 수 있도록 
axis('equal')함수를 사용했습니다.

원형 그래프는 그래프만으로는 정보 전달이 부족하기 때문에
범례나 레이블 등 추가 정보를 포함해서 작성하는 것이 좋습니다.
범례는 legend() 함수를 이용해서 추가할 수 있고, 레이블은 labels 옵션이나
autopct 옵션을 이용할 수 있습니다.
'''

#범례와 레이블을 함께 나타내보자.
figure = plt.figure()
axes = figure.add_subplot(111)
data = [1, 2, 3]
label = ['Good', 'Bad', 'Normal']
axes.pie(data, labels=label, autopct='%d%%')
plt.axis('equal')
plt.legend(label, loc="center left")
plt.show()

'''
autopct 옵션은 문자열 포멧팅을 활용하기 떄문에 소수점 표현도 가능
%% : %를 화면에 표시합니다 -> % 문자는 문자열 포맷팅의 첫 번째 문자로 사용되는 이스케이프
문자이기 때문에 %%처럼 작성해야함.
%0.2f : 소수점을 2자리 표시함 ex) 2.55
%0.1f : 소수점을 1자리 표시함 ex) 3.5
%0.2f%% : 소수점을 2자리 표시 + % ex) 2.55%
%0.1f%% : 소수점을 1자리 표시 + % ex) 3.5%
%d : 정수로 표시 ex) 3
%d%% : 정수와 % 표시 ex) 3% 
'''

'''
깜짝 문제 )
study, sleep, game, etc 3개의 범례를 가지고 
하루를 기준으로 pie차트를 그려보자 
24
study - 4
sleep - 8
game - 3
etc - 9
'''

figure = plt.figure()
axes = figure.add_subplot(111)
data = [4, 8, 3, 9]
label = ['study', 'sleep', 'game', 'etc']
axes.pie(data, labels=label, autopct="%d%%")
plt.axis('equal')
plt.legend(label, loc="center left")
plt.show()


































