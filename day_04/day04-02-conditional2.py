"""
파일 : day04-02-conditional2
개요 : if-else
책 : 94 ~ 95
"""

'''
if는 조건문이 True 일때만 실행문이 동작했지만.
if-else 문은 조건식을 만족하는 경우와 만족하지 않는 경우를 '구분' 하여 코드를 
작성할 때 사용합니다.

if-else 문의 기본 구조는 다음과 같습니다.

if 조건식:
    조건식이 True 일때 실행문
else:
    조건식이 False 일때 실행문 
    
# 순서도 그리기
'''

# 예시 ) 다음은 어떤 변수 a에 저장된 값이 0보다 크거나 같으면 '양수'를 출력하고,
# 0보다 작으면 '음수'를 출력하세요.

# a = -1
# if a >= 0: # True
#     print('양수')
# else:   # False
#     print('음수')

# 예제 ) 값을 입력받아서 해당 값이 짝수인지 홀수인지 출력하세요!

# num = int(input('정수를 입력해주세요 >>> '))
# if (num % 2) == 0:
#     print('짝수')
# else:
#     print('홀수')
    
'''
예제 ) 문자열 입력받고 해당 문자열이 Hello Python안에 포함 되어있는지 확인 후
조건에 따라 다음과 같이 출력해보자.
포함
    "포함되어있음"
비포함
    "포함되어있지 않음"
    
입력 'H'
'H'ello Python
출력 - 포함되어있음 
'''

HELLO_PYTHON = 'Hello Python'

# s = input('문자열을 입력해주세요 >>')
#
# if s in HELLO_PYTHON:
#     print('포함되어있음')
# else:
#     print('포함되어있지 않음')

# 책 예제 ) 다음은 나이를 입력받아 20살 '이상' 이면 '성인', 20살 '미만' 이면 '미성년자'를
# 출력하게 만들어보자.
'''
예시 
입력 - 22 
출력 - 성인
'''

# age = int(input('나이 :'))
#
# if age >= 20:
#     print('성인')
# else:
#     print('미성년자')

'''
( if-else )
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

score = input('점수를 입력해주세요 >>')
score = int(score)
grade = ''

if score >= 90: # 90 이상
    grade = 'A'
else: # 89 이하
    if score >= 70:
        grade = 'B'
    else: # 69점 이하
        if score >= 60:
            grade = 'C'
        else: # 59점 이하
            if score >= 40:
                grade = 'D'
            else:
                grade = 'F'
        
print(f"입력된 학생의 성적 등급은 {grade} 입니다.")
    
    
    
    
    
    
    
    
    