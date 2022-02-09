"""
파일명 : day03-03-collection3
개요 : 딕셔너리와 세트
"""

'''
3. 딕셔너리 dict 
    딕셔너리(dict)는 말 그대로 사전을 의미합니다. 
    사전이란 어떤 단어와 그 단어의 의미로 구성되는데, 파이썬의 딕셔너리도
    역시 같은 구성을 가지고 있습니다. 
    파이썬에서는 'key'와 'value'을 단어와 단어의 의미처럼 사용합니다.

ps. 책을 사면 목차가있는데 그 목차에 있는 목록들이 key! 그 목록에 에 해당하는 페이지 
    내용이 value!!
ps. 목차에는 같은 목록이 있을리가없어요 딕셔너리는 중복된 key 값이 존재하면 
    덮어쓰기됨

딕셔너리의 기본 구조는 다음과 같습니다.
dict = { 
    'key': 'value',
    'key2':'value' 
}    

딕셔너리는 순서가 없는 자료형이였으나 3.7버전 이후로는 저장된 순서대로 접근이 가능합니다.
- 'key' 값으로 이용해서 접근하는 방식을 가장 많이 사용합니다. 

Java에서는 Map 자료형이 dict와 유사함 
'''

d = {
    'a': 'apple',
    'b': 'banana'
}
print(d)
print(type(d))
print(d['b'])

'''
- 딕셔너리의 요소 추가, 수정, 삭제
    3.1 딕셔너리에 요소 추가
        딕셔너리에 새로운 데이터(요소)를 추가하는 방법은 매우 매우 간단합니다. 
        - dict[key] = value
        - dict.setdefault(key, value)
'''
# 변수 선언 ( dict 타입 )
'''
변수 선언 방법
1. 변수명 = {}
2. 변수명 = dict()
'''
d = {}
d['a'] = 'apple'
d['b'] = 'banana'
print(d)

'''
    3.2 딕셔너리의 요소 수정
    딕셔너리에 있는 요소에 대해 수정하는 방법도 매우 간단합니다.
    - dict[key(수정할려는 key)] = 값 **
    - dict.update(수정할려는 key=값)
'''
dic = {'apple' : '사과'}
dic['watermelon'] = '멜론'
print(dic)
# 덮어쓰기 !!!
dic['watermelon'] = '수박'
print(dic)

me = {}
me.setdefault('name', 'Alic') # 추가 setdefault('key', value)
me.setdefault('age', 20)
print(me)
me.update(name='Alice') # 수정 update(key=value)
me.update(age=18)
print(me)

me = {'name': 'Alic', 'age': 20}
me['name'] = 'Alice'
me['age'] = 18

'''
    3.3 딕셔너리의 삭제 
        딕셔너리에 있는 요소를 삭제하는 방법은 다음과 같습니다.
        ( 현업에서는 '삭제' 라는게 할 일이 거의 없다. ) ** 
        - dict.pop(삭제하려는 key)
        - del dict(삭제하려는 key)
'''
me = {'name': 'Alic', 'age': 20}
me['name'] = 'Alice'
me['age'] = 18

me.pop('name')
print(me)

del me['age']
print(me)

# 수정, 삭제 !!! 정말 긴장하고 확인하고 또 확인해보고 동작하는 것

'''
예제) 이름이 Alice, 나이가 18살이고, 사는곳이 서울광역시 xxx동 xx번지
dict로 만들고 나서 출력을 다음과 해주세요
이름 : "Alice"
나이 : "18"
주소 : "서울광역시 xxx동 xx번지"
'''

name = 'Alice'
age = 18
address = '서울광역시 xxx동 xx번지'

info = {
    'name': name,
    'age': age,
    'address': address
}

print(f'이름 : \"{info["name"]}\"')
print(f'나이 : \"{info["age"]}\"')
print(f'주소 : \"{info["address"]}\"')

'''
예제 ) 사용자 정보(이름, 나이(문자열), 주소)를 입력받아서 사용자가 원하는 정보를 보여주세요.
- 이름 : Alice 
- '이름'을 보고싶어요 !

이름을 입력하세요 >>>
나이를 입력하세요 >>>
주소를 입력하세요 >>>
원하는 정보를 입력하세요 >>>
선택하신 정보는 '이름' 이고 값은 Alice 입니다.
'''

name = input('이름을 입력하세요 >>>')
age = input('나이를 입력하세요 >>>')
address = input('주소를 입력하세요 >>>')
info = {
    '이름': name,
    '나이': age,
    '주소': address
}
want = input('원하는 정보를 입력하세요 >>>')
print(f"선택하신 정보는 '{want}'이고 값은 {info[want]} 입니다.")








