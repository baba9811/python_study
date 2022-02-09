"""
파일명 : day06-03-quiz
개요 : 응용 예제
page : 141 ~ 143
"""

'''
책 예제 ) 현재 10000원을 가지고 있습니다. 얼마를 사용할 것인지 반복해서 
입력받아서 10000원을 모두 사용하세요.
0 이하의 금액은 사용할 수 없으며, 현재 가지고 있는 돈보다 더 큰 금액도 사용할 수 없습니다.
* 무한루프, break 활용
출력 예시 )
현재 10000원이 있습니다.
사용할 금액 입력 >>>5000
현재 5000원이 있습니다.
사용할 금액 입력 >>>6000
1000원이 부족합니다.
사용할 금액 입력 >>>-5000
0 이하의 금액은 사용할 수 없습니다.
사용할 금액 입력 >>>5000
현재 0원 이있습니다. 
끝 
'''

# money = 10000
#
# while True:
#     if money != 0:
#         print(f'현재 {money}원이 있습니다.')
#         pay = int(input('사용할 금액 입력 >>>'))
#
#         if pay <= 0:
#             print('0 이하의 금액은 사용할 수 없습니다.')
#         elif (money - pay) < 0:
#             print(f'{pay - money}원이 부족합니다.')
#         else:
#             money -= pay
#             continue
#     else:
#         print('현재 0원이 있습니다')
#         break

'''
책 예제 ) 영화 평점을 1부터 5사이의 정수로 입력받아서 해당 평점만큼
★을 표시하는 프로그램을 구현하세요.
표시할 수 있는 평점의 범위를 벗어나면 재입력을 요구하세요.
★ = ㅁ + 한자 8

출력 :
이번 영화의 평점을 입력하세요 >>>10
평점은 1~5 사이만 입력할 수 있습니다.
이번 영화의 평점을 입력하세요 >>>-2
평점은 1~5 사이만 입력할 수 있습니다.
이번 영화의 평점을 입력하세요 >>>5
평점 : ★★★★★
'''

# star = ''
# while True:
#     score = int(input('이번 영화의 평점을 입력하세요 >>>'))
#     if score <= 0 or score >= 6:
#         print('평점은 1~5 사이만 입력할 수 있습니다.')
#     else:
#         for i in range(score):
#             star += '★'
#         break
# print(f'평점 : {star}')

'''
142 page 
책 예제 ) 저장된 비밀번호를 맞히는 프로그램을 구현하세요.
저장된 비밀번호는 'qwerty'이며 최대 5번 시도할 수 있습니다.
5번 이내에 비밀번호를 맞히면 '비밀번호를 맞혔습니다'를 출력하고.
그렇지 않으면 '비밀번호 입력 횟수를 초과했습니다'를 출력하세요.

출력 예시 )
- 5번 이내 성공
비밀번호를 입력하세요 >>>12345
비밀번호를 입력하세요 >>>asdgagd
비밀번호를 입력하세요 >>>qwerty
비밀번호를 맞췄습니다

- 5번 이내 실패
비밀번호를 입력하세요 >>>12345
비밀번호를 입력하세요 >>>asdas
비밀번호를 입력하세요 >>>qweas
비밀번호를 입력하세요 >>>azsxd
비밀번호를 입력하세요 >>>apapa
비밀번호 입력 횟수를 초과했습니다.
'''

# PWD = 'qwerty'
# count = 5 # 입력 가능 횟수
# while True:
#     if count == 0:
#         print('비밀번호 입력 횟수를 초과했습니다.')
#         break
#     else:
#         input_pwd = input('비밀번호를 입력하세요 >>>')
#         if PWD == input_pwd:
#             print('비밀번호를 맞췄습니다.')
#             break
#         else:
#             count -= 1

'''
책 예제 ) 다음 조건을 만족하는 구구단을 출력하세요.
- 짝수인 (2, 4, 6, 8)단은 출력하지 말고 blank line(줄넘김)만 추가하세요.
- 각 단까지만 출력하는데, 3단이면 3x3까지, 5단이면 5x5까지만 출력.
출력 예 )
3x1 = 3
3x2 = 6
3x3 = 9

5x1 = 5
...
5x5 = 25

...

9x1 = 9
...
9x9 = 81
'''

# dan = 1
# while True:
#     if dan == 1:
#         dan += 1
#         continue
#     elif dan > 9:
#         break
#     elif dan % 2 == 0:
#         print('')
#         dan += 1
#     elif dan % 2 != 0:
#         for i in range(1, (dan + 1)):
#             print(f'{dan} x {i} = {dan * i}')
#         dan += 1

for dan in range(2, 10):
    if dan % 2 != 0:
        for i in range(1, (dan + 1)):
            print(f'{dan} x {i} = {dan * i}')
    else:
        print('')



