"""
파일명 : day05-04-loop5
개요 : 비시퀀스와 for문
page : 126 ~ 128
"""

'''
1. for문과 set
set은 비시퀀스 자료형이기 때문에 저장된 요소들 사이의 순서가 없습니다.
for문을 이용해서 저장된 요소를 부르면 
순서에는 상관없이 하나씩 꺼내서 사용할 수 있습니다.

for 요소 in {세트}:
    반복 실행문
'''

for item in {'가위', '바위', '보'}:
    print(item)

# 순서가 없이 랜덤하게 출력된다 !!! ****

'''
2. for문과 딕셔너리
파이썬의 dict는 순서가 없는 비시퀀스 자료형입니다.
key와 value의 조합으로 데이터를 구성하기 떄문에
value만으로 데이터를 구성하는 리스트, 튜플과 같은 시퀀스 자료형과는
다른 for문의 사용법을 가집니다. 
'''

'''
책 예시 ) 한 사람의 정보를 저장하고 있는 person이라는 딕셔너리를 다음과 같이 생성하고
생성한 person을 이용해 for문을 출력해보자.
'''

person = {
    'name' : '에밀리',
    'age' : 20
}

for item in person:
    print(item)
# value가 아닌 'key'값이 item변수로 전달됨
# 따라서 사용할려면 person[item]으로 출력해야함.

for key in person:
    print(person[key])
    # print(person.get(key))
    
# 책 예시 ) dict 자료형으로 간단한 영어 사전을 구현하고
# 영어 사전에 등록된 모든 단어와 그 단어의 의미를 출력하는 프로그램을 만들어보자

eng_dict = {
    'sun' : '태양',
    'moon' : '달',
    'star' : '별',
    'space' : '우주'
}

for word in eng_dict:
    print(f'{word}의 뜻은 {eng_dict[word]}입니다.')

'''
예제 ) 5개의 문자열을 입력받는데 받을때 뜻까지 포함해서 받고.
5개가 다 입력되고 나서 내가 원하는 문자열을 입력했을때 해당 문자열의 값을 출력하세요
출력 예시 ) 
1번 문자열 입력해주세요 >>> sun
sun의 뜻을 입력해주세요 >>> 태양
2번 문자열 입력해주세요 >>> moon
moon의 뜻을 입력해주세요 >>> 달
.
.
.
영어를 입력해주세요 >>>sun
sun의 뜻은 태양입니다.
'''
d = {}
# index = 1
# for i in range(1, 3):
#     key = input(f'{i}번 문자열 입력해주세요 >>>')
#     value = input(f'{key}의 뜻을 입력해주세요 >>>')
#     d[key] = value
#
# input_key = input('영어를 입력해주세요 >>>')
# print(d[input_key])

index = 1
while len(d) < 5:
    key = input(f'{index}번 문자열 입력해주세요 >>>')
    value = input(f'{key}의 뜻을 입력해주세요 >>>')
    if key not in d:
        d[key] = value
        index += 1














