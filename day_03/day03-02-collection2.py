"""
개요 : 튜플이란?
"""

'''
2. 튜플 
    튜플은 한마디로 요약해서 저장된 값을 변경할 수 없는 리스트입니다.
    리스트와 마찬가지로 각 요소마다 인덱스가 부여되고 슬라이싱도 지원됩니다.
    다만 이미 저장된 값 이외에는 추가, 수정, 삭제가 불가합니다.
    
2.1 선언 방법
    - 선언 방법은 2가지 입니다.
        2.1.1 소괄호 이용 : (값1, 값2, 값3...)
        2.1.2 tuple 함수 이용 : tuple(반복가능객체)

* 소괄호 이용할때 값이 한개만 들어가는 경우 ','를 함께 작성해야함.
   안하면 튜플이 아니라 그냥 값으로 인식됨.
'''

t1 = (1, 2, 3)
print(t1)
print(type(t1))
t2 = 1, 2, 3
# t2, t3, t4 = 1, 2, 3 하면 각각 정수 타입으로 선언됨
print(t2)
print(type(t2))

t3 = tuple([100, 3.14, 'hello'])
print(t3)
print(type(t3))

t4 = (100)
# 연산자 () 하면 먼저 계산!!!
print(type(t4))

t5 = (100, )
print(type(t5))

# 추가 수정 삭제 ???
t1 = (100, 200, 300)
print(type(t1))
# t1[0] = 110 수정
print(t1)
# del t1[0] 삭제 
