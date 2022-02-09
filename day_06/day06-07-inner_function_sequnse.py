"""
파일명 : day06-07-inner_function_sequnse
개요 : 시퀀스 내장 함수
page : 154 ~ 159
"""

'''
1. enumerate() 함수 ***
enumerate() 함수를 '리스트와 함께 사용'할 수 있습니다.
enumerate() 함수를 사용하면 '리스트에 저장된 요소'와 
'해당 요소의 인덱스'가 튜플 형태로 함께 '추출'됩니다.

리스트와 enumerate() 함수를 함께 사용하는 방식은 다음과 같습니다.
for 변수 in enumerate(리스트):
    반복실행문
'''
for item in enumerate(['가위', '바위', '보']):
    print(item)

# 언패킹 **
for i, v in enumerate(['가위', '바위', '보']):
    print(f'index = {i} // value = {v}')

'''
2. range() 함수
range() 함수는 '전달된 인수 값에 따라' 시퀀스 자료형의 데이터를 생성하는 함수입니다.
'특정 범위의 값을 생성'하기 때문에 범위 생성자라고도 합니다.

주로 사용되는 곳은 for문이며 원하는 횟수만큼 for문 내부의 실행문을 실행합니다.
range() 함수의 결과 자료형은 'range'이기 때문에 list() 함수나 tuple() 함수를 통해서
변환해서 사용합니다.

range() 함수의 사용법은 다음과 같습니다.
1. range(stop)        - range(10)
2. range(start, stop) - range(1, 11)
3. range(start, stop, step) - range(1, 11, 2)
'''

'''
range(stop)
'0부터 stop 사이의 모든 정수가 생성'됩니다.
생성되는 정수를 n이라고 하면 n의 범위는 0 <= n < stop
'''

'''
range(start, stop)
start부터 stop 사이의 모든 정수가 생성됩니다.
생성되는 정수를 n이라고 하면 n의 범위는 start <= n < stop 입니다.
'''

'''
range(start, stop, step)
start부터 stop 사이의 정수 중에서 step 만큼의 차이를 가지고 있는 정수가 생성됩니다.
range(1, 10, 2) [1, 3, 5, 7, 9]
'''
print(list(range(1, 11, 2)))

'''
4. len() 함수
len() 함수에 '전달된 객체'의 '길이(항목 수)'를 '반환'하는 함수입니다.
li = ['a', 'b', 'c', 'd']
len(li)
4
len(range(10))
10
'''

'''
5. sorted() 함수
sorted() 함수에 전달된 반복가능객체의 오름차순 정렬 결과를 반환합니다.
reverse=True 옵션을 추가할 경우 내림차순 정렬 결과를 반환합니다.
'''
li = [6, 3, 1, 2, 4, 5]
print(sorted(li))
print(sorted(li, reverse=True))

# * sorted 함수를 이용했다고 변수에 있는 값이 변경되는건 아니다.
li = [6, 3, 1, 2, 4, 5]
print(sorted(li))
print(li)

# sorted 함수는 정렬된 결과를 반환해줌.
li = [6, 3, 1, 2, 4, 5]
li = sorted(li)

'''
6. zip() 함수
zip() 함수는 전달된 여러 개의 반복가능객체의 각 요소를 튜플로 묶어서
반환하는 함수입니다.

* 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체를 기준으로 동작합니다.
'''

# 책 예시
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
print(tuple(zip(names, scores)))
for student in zip(names, scores):
    print(student)

'''
책 예제 ) 다음은 리스트에 월별 일수를 저장해 두고 1월부터 12월까지 월별 일수를 
출력하는 프로그램입니다. 윤년은 고려하지 않고 모두 평년이라고 가정했음.
( 윤년은 2월이 29일까지 있지만 여기슨 평년으로 했기에 28 )
[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
출력 : 
1월 = 31
2월 = 28
3월 = 31 
'''

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months, start=1):
    print(f'{month}월 = {day}일')
















