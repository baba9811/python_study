"""
파일명 : day01-01-comment.py
개요 : 주석에 대한 설명
작성일 : 2021-06-26
"""

# 이것은 한줄 주석입니다. print()
# 번역 X ( 개발자가 볼때만 )

''' 
이것은 여러줄 주석입니다.
이것은 print해주는 함수입니다.
'''
def plus(a, b):
    a + b

"""
docString <- 문서를 만들때 사용 
모듈, 함수, 클래스, 메소드 
1. 모듈 - 파이썬 .py 
2. 함수 - 특정 기능하는 프로그램 코드의 집합
3. 클래스 - 객체를 생성하기 위한 설계도
4. 메소드 - 클래스 내부의 함수 = cul.action()
"""

# 계산 객체를 만들었다.

class cul():
    # 변수
    goods = ['사탕', '사이다', '콜라']

    # 메소드
    def action(self):
        a = 1
        b = 2
        a + b



def plusTwoPlus(a, b, c):
    a + b
    a + c
    b + c


plusTwoPlus(1, 2, 3)
