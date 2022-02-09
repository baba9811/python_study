"""
개요 : 컬렉션, List
page : 39 ~
"""

'''
컬렉션이란 모음이라는 뜻을 가지고있고 파이썬에서 컬렉션은 다음과 같은 의미를 가지고있습니다.
'여러 값을 하나의 이름으로 묶어서 관리하는 자료형'

python에서 컬렉션은 다음과 같은 종류가 있습니다.
1. List ( 리스트 )
2. tuple ( 튜플 )
3. set ( 세트 )
4. dict ( 딕셔너리 )

** 컬렉션 중에서 저장된 값들의 순서가 있는 컬렉션을 '시퀀스'라고 부릅니다.
리스트와 튜플이 대표적인 시퀀스입니다. 
'''

st = 'abcd'
'     0123'
#    [ 'a', 'b', 'c', 'd' .... ]
#       0    1    2    3 ....
# set 같은 경우에는

s = set()
s.add('a')
s.add('b')
# .... 'a', 'b' .. 순서대로 넣었으니 순서대로 나올 것같은데...?
# 'b', 'a' 이렇게 순서없이 나올 수 있다.

'''
1. List - 리스트
여러 값을 저장할 때 가장 많이 사용하는 자료형.
저장하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장할 수 있습니다.
int, float, str, bool

Java 
List<String> li = new ....();
li안에는 꼭 String!! 

-- 
리스트 초기화 방법은 2가지가 있습니다.
1. 변수명 = [값1, 값2, 값3 ....]
2. 변수명 = list([값1, 값2, 값3 ...])
           list(반복할 수 있는 객체) 
'''

# 1. 변수명 = []
li = [10, 10.2, 'ab', True]
print(li)

# list() 함수 이용
li = list([10, 10.2, 'ab', True])
li = list('abcdf')
print(li)

li = []
li.append(10)
li.append(10.2)
li.append('ab')
li.append(True)

print(li)

'''
1.1 리스트 인덱스와 슬라이싱
    1.1.1 리스트 인덱스
        리스트는 문자열과 동일하게 인덱싱을 지원하며 저장된 '요소'들 마다 고유 번호인 인덱스를
        부여하여 순서대로 관리할 수 있습니다.
        - 사용방법 : list[index]
        
    1.1.2 리스트 슬라이싱
        문자열과 동일하게 슬라이싱 기능을 이용할 수 있습니다. 리스트 속 원하는 일부 
        요소만 이용하고자 하는 경우에 사용할 수 있습니다.
        - 사용방법 : list[start, end, step]
'''
st = 'abcd'
print(li[1])
print(st[1])

test_list1 = ['10', 20, '30', 40, '50', 60, '70']
#              0    1    2     3    4    5    6

# [ 20, '30', 40 ]
print(test_list1[1:4])

'''
1.2 리스트 요소의 추가, 수정, 삭제
    1.2.1 요소 추가
        리스트에 새로운 요소를 추가할 때는 append()와 insert() 메소드를 사용할 수 있습니다.
        - 사용방법 : list.append(추가할 요소)
                    list.insert(index, 추가할 요소)
                    
    1.2.2 요소 수정 
        리스트 요소중 수정을 원할때는 index를 이용해서 수정을 진행한다.
        - 사용방법 : list[수정할 index] = 수정될 값
    
    1.2.3 요소 삭제
        리스트 요소중 삭제를 원할때는 pop(), del, remove()을 이용해서 삭제를 진행한다.
        - 사용방법 : pop(index) - index 작성 없으면 기본 값은 맨 마지막 요소 
                    del list[index] - 슬라이싱도 사용 가능함 
                    remove(삭제 요소) - 제일 먼저 만나는 요소 삭제
'''

# 1.2.1 요소 추가
# append
# 뒤에 계속 추가
# 10, 20, 30, 40...
li = []
li.append(10)
li.append(20)
print(li)

# insert
# 내가 원하는 인덱스에 직접 넣을 수 있다.
li.insert(0, 'ab')
print(li)


# 1.2.2 요소 수정
# list[index] = value
li[2] = '30'

print(li)

# 1.2.3 요소 삭제
# list.pop(index)
# del list[index]
# list.remove(삭제 요소)

li.append('30')
li.append('30')
li.append('40')
print(li)
# pop(index)
li.pop(0)
print(li)
# del 객체
# 슬라이싱 사용 가능
del li[0:2]
print(li)
# remove(삭제 요소)
# 0, 1번째 인덱스에 '30'이 있었는데 뭐가 지워졌냐??
# 제일 먼저 만나는거 순서로 지웁니다.
li.remove('30')
print(li)

'''
1.3 리스트 기타 함수 
    1.3.1 리스트 길이(요수 수) 구하기 
        리스트에 요소가 몇개 들어있는지 원할때 len() 함수를 사용한다.
        - 사용방법 : len(list)
    1.3.2 리스트 요소 정렬
        리스트에 있는 요소를 정렬해줘야할때 sort() 메소드를 사용한다.
        - 사용방법 : list.sort()
        - sort(reverse)에 따라 오름차순 내림차순이 결정된다. ( 생략가능 )
         - True : 내림차순
         - False : 오름차순
    1.3.3 리스트 요소 뒤집기
        리스트에 있는 요소의 순서를 역순으로 뒤집어줍니다. ( 정렬 x )
        - 사용방법 : list.reverse()
    
    1.3.4 리스트 요소 위치 반환
        리스트에 원하는 요소의 위치 값을 알려줍니다.
        - 사용방법 : list.index(원하는 요소)
        * 없는 값 쓰면 에러!!!
        
    1.3.5 리스트 요소중 원하는 요소 갯수 확인
        원하는 요소가 리스트 속에 몇 개 있는지 파악합니다.
        - 사용방법 : list.count(확인하고싶은 요소)
'''
li = [20, 30, 40, 50]
# li = [?]
print(len(li))
print(len('str'))
# 요소 정렬
# reverse
li = [30, 60, 40, 20]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

# 요소 뒤집기
li = [20, 60, 40, 30]
li.reverse()
print(li)

# 요소 위치 반환
li = [20, 50, 60, 30]
#      0   1   2
print(li.index(60))

# 요소 갯수 확인
li = [30, 40, 50, 30, 30]
print(li.count(30))

