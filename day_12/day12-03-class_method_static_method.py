"""
파일 : day12-03-class_method_static_method
개요 : 클래스 메소드와 정적 메소드
page : 278 ~ 282
"""

'''
1. 클래스 변수
[ 인스턴스 변수 ]
- 클래스를 구현할 때 인스턴스마다 서로 다른 값을 가지는 경우   
    -> 인스턴스 변수를 사용
    -> self 키워드를 붙여서 사용
[ 클래스 변수 ]
- 인스턴스들이 서로 같은 값을 가지는 변수 

예시 ) 한국 사람을 클래스로 구현한다
[ 인스턴스 변수 ]
- 이름, 나이, 주소 등 
[ 클래스 변수 ]
- 한국 사람

[ 클래스 변수 사용하는 이유 ]
- ** 메모리 공간을 낭비를 막을 수 있습니다.
'''
class Korea:

    # 클래스 변수 country
    country = '한국'

    # 생성자
    def __init__(self, name, age, address):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.address = address

man = Korea('홍길동', 35, '서울')
print(man.name)

# print(Korea.name)
# AttributeError: type object 'Korea' has no attribute 'name'

print(man.country)
print(Korea.country)

'''
[ 구분 ]

인스턴스 변수 
    - 목적 : 인스턴스 마다 다른 값을 저장
    - 접근 방식 : 인스턴스 접근 (O)
                 클래스 직접 접근 (X)
    
클래스 변수
    - 목적 : 인스턴스가 공유하는 값을 저장
    - 접근 방식 : 인스턴스 접근 (O)
                 클래스 직접 접근 (O)

* 클래스 변수는 클래스를 통해서 접근하는 것이 권장 사항
'''
'''
2. 클래스 메소드
클래스 메소드 = 클래스 변수를 사용하는 메소드

[ 클래스 메소드의 주요 특징 ]
- 인스턴스 또는 클래스로 호출합니다.
- 생성된 인스턴스가 없어도 호출 할 수 있다.
- @classmethod 데코레이터를 표시하고 작성합니다.
- 매개변수 self (X) -> cls를 사용합니다.

[ 호출 방식 차이 ]
- 인스턴스를 통해서 호출 X -> 클래스.메소드()와 같은 형식으로 호출
- self 사용 X -> cls를 통해서 클래스 변수에 접근 
    ->> 인스턴스 메소드와 가장 큰 차이점.
'''
class Korea:

    # 클래스 변수 country
    country = '한국'

    # 클래스 메소드야~!!!! 하고 알려주는 데코레이터
    @classmethod
    def trip(cls, country):
        # cls == class == 현재 여기선 Korea class
        # cls.country == Korea.country
        if cls.country == country:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korea.trip('한국')
Korea.trip('미국')

import datetime
from datetime import *

# datetime 클래스 메소드
print(datetime.now())

'''
3. 정적 메소드
self X -> 인스턴스 변수를 사용하지 않는다 ( 사용할 수 없음 )
cls X -> 클래스 변수를 사용하지 않는다.

[ 정적 메소드의 특징 ]
- 인스턴스 또는 클래스로 호출
- 생성된 인스턴스가 없어도 호출
- @staticmethod 데코레이터를 표시하고 작성
- 반드시 작성해야 할 매개변수 X

[ 즉 ]
self, cls X -> 인스턴스에는 영향을 주지 않고 또한 인스턴스로부터 영향을 받지도 않음.
'''
class Korea:
    
    country = '한국'

    # 정적인 메소드로 사용할꺼야!!!
    @staticmethod
    def slogan():
        # 인스턴스 변수, 클래스 변수 모두 사용하지 않음.
        print('Imagine your Korea')

# 인스턴스 생성 없이 호출할 수 있는게 장점
Korea.slogan()

'''
[ 정적인 메소드 사용처 ]
현업 기준
-> Utils 도구 모음 할때 사용을 많이함.
예시 ) Java - isEmpty()
    -> ()안에 들어온 리스트가 null or length == 0 > true
    
a = '' 

class CommonsUtils:

    @staticmethod
    def isEmpty(a):
        if a:
            return true
        else:
            return false 
            
if(CommonsUtils.isEmpty()):
    xxxx
'''

'''
책 예제 ) 다음은 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 
계산할 수 있는 Bag 클래스이다
'''
class Bag:

    # 클래스 변수
    count = 0

    def __init__(self):
        Bag.count += 1

    # 클래스 메소드
    @classmethod
    def sell(cls):
        cls.count -= 1

    # 클래스 메소드
    @classmethod
    def remain_bag(cls):
        return cls.count

print(f'현재 가방 {Bag.remain_bag()}개')
# bag1 = Bag()
Bag()
Bag()
Bag()
print(f'현재 가방 {Bag.remain_bag()}개')
# bag1.sell()
Bag.sell()
Bag.sell()
print(f'현재 가방 {Bag.remain_bag()}개')


















