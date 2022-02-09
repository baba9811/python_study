"""
파일명 : day06-08-inner_function_quiz
개요 : 응용문제
page : 160
"""

'''
책 예제 ) 무지개의 일곱 색깔을 저장하는 rainbow 리스트를 생성하고
다음과 같이 출력하세요.
출력 :
무지개의 1번째 색은 red입니다.
무지개의 2번째 색은 orange입니다.
무지개의 3번째 색은 yellow입니다.
무지개의 4번째 색은 green입니다.
무지개의 5번째 색은 blue입니다.
무지개의 6번째 색은 navy입니다.
무지개의 7번째 색은 purple입니다.
'''
#
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# for index, color in enumerate(rainbow, start=1):
#     print(f'무지개의 {index}번째 색은 {color}입니다.')

'''
책 예제 ) 어떤 학생의 점수를 입력받아 평균 점수, 최고 점수, 최저 점수를 구하는 
성적 계산 프로그램을 구현하세요,
다음 지시사항을 고려하여 구현하세요.
# 몇 개의 점수를 입력받아야 하는지 모르는 상황임.
# 0보다 작은 점수를 입력하면 더 이상 입력할 점수가 없음을 의미합니다.
# 입력받은 모든 점수는 exam 리스트에 저장합니다. 
# 마지막에 입력된 0보다 작은 점수는 exam에 저장하지 않습니다.

출력 :
점수를 입력하세요. 더 이상 입력할 점수가 없다면 음수를 아무거나 입력하세요.
점수 입력 >>>80
점수 입력 >>>50
점수 입력 >>>60
점수 입력 >>>30
점수 입력 >>>90
점수 입력 >>>-1
평균 = 62.0, 최대 = 90, 최소 = 30
* 평균은 '합계/개수'로 구합니다.
'''

# scores = []
# print('점수를 입력하세요. 더 이상 입력할 점수가 없다면 음수를 아무거나 입력하세요.')
# while True:
#     score = input('점수 입력 >>>')
#     score = int(score)
#     if score < 0:
#         break
#     else:
#         scores.append(score)
#
# print(f'평균 = {sum(scores) / len(scores):.2f}, 최대 = {max(scores)}, 최소 = {min(scores)}')

'''
예제 ) 영화관 어플에서 재예매율 혹은 평점에 대해 얻는 프로그램을 짜려고한다.
주어진 영화 정보를 가지고 사용자가 입력한 원하는 정보에 따라 해당 값이 출력되게 해보자.
( 한 번만 동작 )

영화 정보 : ['컨져링', '블랙위도우', '크루엘라']
각각 평점 : ['8', '9', '9']
재예매율 : [70, 74, 2]

출력 :
어떤 것을 확인하시겠습니까?(재예매율, 평점) >>> 재예매율
어떤 영화를 확인하시겠습니까?(컨져링, 블랙위도우, 크루엘라) >>> 컨져링
선택하신 영화는 컨져링이고 해당 영화의 재예매율 정보는 8입니다.
'''
# 1. if
# category = ['재예매율', '평점']
# name = ['컨져링', '블랙위도우', '크루엘라']
# score = ['8', '9', '9']
# reticket = [78, 74, 2]
#
# # {key : value ..}
# reticket_dict = dict(zip(name, reticket))
# score_dict = dict(zip(name, score))
#
# category_input = input(f'어떤 것을 확인하시겠습니까? {category} >>>')
# name_input = input(f'어떤 영화를 확인하시겠습니까? {name} >>>')
# if category_input == category[0]:
#     print(f'선택하신 영화는 {name_input}이고 해당 영화의 {category_input} 정보는 '
#           f'{reticket_dict[name_input]} 입니다.')
# else:
#     print(f'선택하신 영화는 {name_input}이고 해당 영화의 {category_input} 정보는 '
#           f'{score_dict[name_input]} 입니다.')



exam = []
print('점수를 입력하세요. 더 이상 입력할 점수가 없다면 음수를 아무거나 입력하세요')
for n in exam: # 요부분 문제입니다. exam은 [] 아무것도 없어서 for문이 동작이 안됩니다.
    score = int(input('점수를 입력하세요'))
    if score < 0:
        break
    exam.append(score)
print(f' 최고 점수 = {max( exam)}, 최저 점수 = {min(exam)}, 평균 점수 ={sum(exam) / len(exam)}')



