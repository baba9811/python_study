"""
파일명 : day03-04-collection4
개요 : 세트란?
"""

'''
4. 세트 - set
    세트는 수학의 집합 개념을 구현한 자료형입니다. 세트에 저장된 값들은 순서가 없기 떄문에
    인덱싱과 슬라이싱을 사용할 수 없습니다.
    대신 중복된 값의 저장이 불가능하다는 특징을 활용해 중복 제거용으로 사용하거나 
    교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용할 수 있습니다. 
    
선언 방법
1. 중괄호 이용 - {} ( 값이 아무것도 없으면 dict 타입으로 저장됩니다. )
    - s = {값1, 값2, 값3}
2. set() 함수 이용
    - s = set(반복가능한객체)
    
JAVA -
    set() 변수로 만들고 내부를 보면 
        info = {   
            "key" : null,
            "key2" : null,
            .....
        }
    외부로 보면
        info => {'key', 'key2'}  
'''

s = {10, 20, 30}
print(type(s))
s = {}
print(type(s))
print(s)

'''
4.1 세트의 요소 추가 
    - 세트에 값을 넣는건 add() 메소드를 이용해야합니다. 
        - set.add(value)
'''

s = {10, 20, 30}
s.add(40)
print(len(s))
s.add(40)
print(len(s))
print(s)
print(len(s))

'''
4.2 세트의 요소 수정 ( x )
    세트는 수정을 지원하지 않습니다. ( 순서가 없어서 )
'''

'''
4.3 세트의 요소 삭제
    세트에 있는 요소를 삭제하는 방법은 다음과 같습니다.
        - set.remove(삭제할 값) 
        - set.discard(삭제할 값)
        둘의 차이는 삭제할 값이 set에 포함되어있지 않을때 
        에러 발생 여부 차이!!!
'''

s = {10, 20, 30, 40}
s.remove(20)
print(s)
# s.remove(50)
s.discard(50)
print(s)

'''
교집합, 합집합, 차집합, 대칭차집합(합집합 - 교집합)
# - 교집합 : & or intersection
# - 합집합 : |(\ + shift) or union
# - 차집합 : - or difference
# - 대칭차집합 : ^(shift + 6) or symmetric_difference
'''
set1 = set([1, 2, 3])
set2 = set([2, 4, 5, 6])

# 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 합집합
print(set1 | set2)
print(set1.union(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))
print(set2.difference(set1))

# 대칭차집합
print(set1 ^ set2)


# 예제 ) set 선언하고 {1, 2} -> 3, 4, 5, 6 -> 4 지우고 -> 6 지우고

s = {1, 2}
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print(s)
s.discard(4)
print(s)
s.discard(6)
print(s)

# 예제 ) List 선언하고 문자 5개 넣고 그걸 set으로 변경한다음 2번째에 있던 문자 지워보기
# [ '1', '2', '3', '4', '5' ](list) -> set -> '2' 삭제

li = []
li.append('1')
li.append('2')
li.append('3')
li.append('4')
li.append('5')
print(li)
s = set(li)
print(s)
s.discard('2')
print(s)

'''
mutable 과 immutable * 표(page.47)
    - mutable : 생성이 된 후에도 변경이 가능한 자료형
        - 리스트에 값을 저장하고 id() 함수로 주소값 확인 후에 list에 값을 추가해도 
            주소값이 변경되지 않은 것을 확인 할 수 있다.
    - immutable : 생성된 후에는 변경이 불가능한 자료형
        - 변수에 정수를 저장하고 id() 함수로 주소값 확인 후에 
            정수를 변경하면 주소값이 변경되는 것을 확인 할 수 있습니다.
    
- 값 변경 후에 주소값 바뀌나?
    
Java
    - class info 
    - main info.name -> 변경 -> 함수를 통해서 info.name받고 
        함수 '내'에서 info.name을 수정하고 return을 안했음.
    - main에서 info.name 찍어보면 
    함수안에 변수를 받을 수 있는데 ( 정수, 실수 )
    
'''

a = 10
print(id(a))
b = 20
print(id(b))
c = 10
print(id(c))

'''
1. mutable
'''

me = [1, 2, 3]
print(id(me))
me.append(4)
print(id(me))

'''
2. immutable
'''

me = 10
print(id(me))
me += 1
print(id(me))

me = [1, 2, 3] # 주소 생성 됬고
you = me    # you = me ( 주소 같다. )
print(id(me))
print(id(you))

# 중요 !! 주소 공유
you.append(4)
print(you)
print(me)

'''
예제 ) 문자열 s에 'maple'이 저장되어 있습니다. 
문자열 s의 가운데 글자를 출력하는 프로그램을 구하세요.
maple의 가운데 글자는 p 입니다.
글자를 홀수 단위로 추가했을때 가운데 글자가 나오게  
s = 'maplell'
s[2]
mapplell의 가운데 글자는 l 입니다. # 연산자, len()
'''

s = 'mapplellsss'
center_str = len(s) // 2
print(s[center_str])

'''
예제 ) 리스트 [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소부터
        7번째 요소만 추출한 결과 리스트에서 2번째 요소를 출력하는 프로그램을 구현하세요.
    - 출력문 -
    3번째 요소부터 7번째 요소 : [30, 40, 50, 60, 70]
    3번째 요소부터 7번째 요소 중 2번째 요소 : 40
'''

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
li37 = li[2:7]
print(li37)
li37_in2 = li37[1]
print(li37_in2)






