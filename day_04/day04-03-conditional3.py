"""
파일 : day04-03-conditional3
개요 : if-elif
책 : 96 ~ 99
"""

'''
if-elif 문을 소개하기 전에 if-else로 다음 상황 해결해 보겠습니다!

중요도가 100이상이면 '상', 중요도가 50~99면 '중', 50 미만은 '하'로 구분하여
출력합니다.
'''

important = 100

if important >= 100:
    print('상')
else: # important 가 100 미만
    if important >= 50:
        print('중')
    else:
        print('하')

'''
이 문제는 if-else 문 하나로는 해결이 되지 않기 떄문에 위와 같이 else 문 내부에
또 다른 if-else 문을 추가하여 해결했음.

이 방법은 구분해야 할 데이터가 많아지면 많아질수록 코드가 굉장히 복잡해지는 
단점이 있습니다.

이러한 단점을 보완하고 보기 좋은 코드를 작성하려면 if-elif가 사용됩니다.

if-elif 문은 특정 조건에 따라 3가지 이상으로 구분해야할때 사용합니다.
( elif - else if )

if 조건식 1:
    조건식 1의 결과가 True일때 실행문
elif 조건식2:
    조건식 1의 결과가 False이고 조건식 2의 결과가 True일때 실행문
elif 조건식3:
    조건식 1,2의 결과가 False이고 조건식 3의 결과가 True일때 실행문
.
.
.
else:
    모든 조건식이 False 일때 사용 
    
* 원하는 만큼 elif 문은 계속해서 추가 할 수 있고 대부분 마지막에 else 문을 추가합니다.
'''

# 예시 ) 다음은 어떤 변수 num에 저장된 값이 0보다 크면
# 0보다 작으면 '음수'를 출력하고 0이면 0 출력


num = -1
if num > 0:
    print('양수')
elif num < 0:
    print('음수')
else:
    print('0')

'''
if 문 만으로 표현도 가능하다.
if num > 0:
    print('양수')
if num < 0:
    print('음수')
if num == 0:
    print('0')
    
** 하지만 매우 비 효율적임 ( num을 중복해서 3번이나 비교해봐야 하기 때문이고,
    내가 원하는 결과를 얻지 못할 수 있음 )
    
예시 ) 만약 a라는 변수 문자열 1개를 입력받는데 입력받은게 1개면 1을 출력시켜주고
    'd'이면 0을 출력시켜주세요!
'''

# a = input('문자 1개 입력')
# b = 0
#
# if a == 'd':
#     b = 0
# print(b)
# if len(a) == 1:
#     b = 1
# print(b)
#
# if a == 'd':
#     b = 0
# elif len(a) == 1:
#     b = 1
#
# print(b)

'''
예제 ) 값을 입력받아서 각 조건에 따라 다음과 같이 출력해주소
0일때 : 입력하신 정수는 0입니다.
짝수일때 : 입력하신 정수는 짝수입니다.
홀수일때 : 입력하신 정수는 홀수입니다.
'''

# num = input('정수를 입력해주세요 :')
# num = int(num)
#
# if num == 0:
#     print('입력하신 정수는 0입니다.')
# elif (num % 2) == 0:
#     print('짝수')
# elif (num % 2) == 1:
#     print('홀수')

'''
책 예제 ) 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요
정수1 입력 >>> 3
정수2 입력 >>> 1
정수3 입력 >>> 2
출력 : 가장 큰 수는 3입니다.
* 관계 연산자( >, >=, <, <=, ==, != ), 논리 연산자 ( and, or, not )
'''

# a = int(input('정수1 입력 >>>'))
# b = int(input('정수2 입력 >>>'))
# c = int(input('정수3 입력 >>>'))
#
# if a == b == c:
#     print('전부 같은 숫자입니다.')
# elif a > b and a > c:
#     print(f'가장 큰 수는 {a}입니다.')
# elif b > a and b > c:
#     print(f'가장 큰 수는 {b}입니다.')
# elif c > a and c > b:
#     print(f'가장 큰 수는 {c}입니다.')
# else:
#     print(f'??? a={a} b={b} c={c}')

if a == b == c:
    print('전부 같은 숫자입니다.')
elif a >= b and a >= c:
    print(f'가장 큰 수는 {a}입니다.')
elif b >= a and b >= c:
    print(f'가장 큰 수는 {b}입니다.')
elif c >= a and c >= b:
    print(f'가장 큰 수는 {c}입니다.')
else:
    print(f'??? a={a} b={b} c={c}')

'''
책 예제 ) 미세먼지 저감 활동의 일환으로 차량 2부제를 실시합니다.
    사용자로부터 차량번호를 입력받아 차량번호가 짝수로 끝나면 '운행가능',
    아니면 '운행불가'를 출력하는 프로그램을 구현하세요.
    * 단, 차량번호는 'xxx가xxxx'와 같은 형식으로 입력받는다는 가정.
    
예시 ) 차량번호를 입력하세요 >>> 237가1234
차량번호 '237가1234'는 오늘 운행가능입니다.
* 49P 2번 ( 마이너스 인덱스 활용하면 쉽게 할 수 있다. )
'''

car_number = input('차량번호를 입력하세요 >>>')
last_car_number = int(car_number[-9])
print(last_car_number)

'''
( if-elif )
예제 ) 성적 등급 표는 다음과 같다. 이를 이용해 학생의 점수를 입력받아 해당되는
점수를 아래와같이 출력해주세요.
표:
    100 ~ 90 : A
    89 ~ 70 : B
    69 ~ 60 : C
    59 ~ 40 : D
    39 ~ 0 : F

출력문 : 입력된 학생의 성적 등급은 'x' 등급 입니다.
예시 ) 88 입력 받으면
입력된 학생의 성적 등급은 'B' 등급 입니다.
'''

score = input('점수를 입력해주세요 : ')
score = int(score)
grade = ''

if score >= 90:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 40:
    grade = 'D'
else:
    grade = 'F'

print(f"입력된 학생의 성적 등급은 '{grade}' 입니다.")












