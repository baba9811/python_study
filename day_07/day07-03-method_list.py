"""
파일 : day07-03-method_list
개요 : 리스트 메소드
page : 174 ~ 177
"""

'''
1. append() 메소드
- 리스트의 끝에 인수로 '()'안에(인수) 전달된 데이터를 추가합니다.
* 리스트의 끝으로 차곡차곡 쌓인다.
'''

li = ['apple', 'banana']
li.append('cherry')
print(li)

'''
2. extend() 메소드
extend() 메소드는 리스트에 다른 리스트나 튜플과 같은 반복가능객체를
추가하여 준 리스트를 반환함
list + list(반복가능객체) 라고 생각하면 편함
'''

li = ['apple', 'banana']
li.extend(['cherry', 'mango'])
li.extend(('bb', 'cc'))
print(li)

'''
3. insert() 메소드
insert() 메소드는 리스트의 특정 인덱스에 데이터를 추가하는 메소드입니다.
insert() 메소드에 전달되는 첫 번째 인수는 인덱스, 두 번째 인수는 저장할
데이터를 의미합니다.
'''

li = ['apple', 'banana']
li.insert(0, 'cheery')
print(li)

'''
4. clear() 메소드
clear() 메소드는 리스트에 저장된 요소를 삭제하는 메소드입니다.
'''

li = ['apple', 'banana']
print(li.clear())

'''
5. pop() 메소드
pop() 메소드를 호출하면 리스트의 마지막 요소가 반환되고, 
해당 리스트에서 반환된 값은 제거됩니다.
* 인덱스 줄 수 있음.
'''

# 인덱스 지정 안 함
li = ['apple', 'banana']
item = li.pop()
print(item)
print(li)

# 인덱스 지정
li = ['apple', 'banana']
item = li.pop(0)
print(item)
print(li)

'''
6. remove() 메소드
remove() 메소드는 인수로 전달된 값과 동일한 요소를 찾아서 제거,
동일한 요소가 여러개 있는 경우는 첫 번째 요소가 제거됩니다
'''

li = ['apple', 'banana', 'cherry', 'mango', 'cherry']
li.remove('cherry')
print(li)

'''
책 예제 ) 다음은 리스트에 포함된 잘못된 데이터를 
모두 제거하는 프로그램입니다.
리스트에 저장된 정상 데이터는 모두 'a'를 포함한 문자열이며,
그렇지 않은 경우 잘못된 데이터입니다.

li = ['above', 'cookie', 'app', 'about', 'admin', 'bisket' ]
출력:
cookie 제거됩니다.
bisket 제거됩니다.
['above', 'app', 'about', 'admin' ]
remove or pop
'''

li = ['above', 'cookie', 'app', 'about', 'admin', 'bisket' ]

for i, item in enumerate(li):
    if item.find('a') == -1:
        print(f'{li.pop(i)} 제거됩니다.')

print(li)

'''
예제 ) basket 이라는 과일을 담는 list형식의 변수가 있다.
이 변수에 과일 10개를 담아보자.

출력:
1번째 과일을 입력해주세요 >>>사과
2번째 과일을 입력해주세요 >>>사과
3번째 과일을 입력해주세요 >>>바나나
...
10번째 과일을 입력해주세요 >>>딸기

과일박스에는 ['사과', '사과', '바나나', .... '딸기']가 들어있습니다.
'''

basket = []
for i in range(1, 11):
    basket.append(input(f'{i}번째 과일을 입력해주세요 >>>'))
print(f'과일 박스에는 {basket}가 들어있습니다')


