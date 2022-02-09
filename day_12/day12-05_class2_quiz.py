"""
파일명 : day12-05-class2_quiz
개요 : 응용문제
page : 287 ~ 289
"""

'''
1. 다음 지시사항을 읽고 이름과 전체 인구수를 저장할 수 잇는 Person클래스를 생성하세요.

[ 지시 사항 ]
- 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요.
man = Person('james')
woman = Person('emily')

- man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is born
emuly is born

- 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 처리하세요.
print(f'전체 인구수: {Person.get_population()}명') # 전체 인수구 2명

- 다음과 같은 방법으로 man 인스턴스를 삭제하세요
del man

- man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is dead

[ 출력 ]
james is born
emily is born
전체 인구수: 2명
james is dead
전체 인구수: 1명
'''
class Person:

    count = 0

    def __init__(self, name):
        Person.count += 1
        self.name = name
        print(f'{self.name} is born')

    @classmethod
    def get_population(cls):
        return cls.count

    def __del__(self):
        Person.count -= 1
        print(f'{self.name} is dead')

man = Person('james')
woman = Person('emily')
print(f'전체 인구수: {Person.get_population()}명')
del man
print(f'전체 인구수: {Person.get_population()}명')

'''
2. 다음 지시사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 구현하세요.

[ 지시사항 ]
- Shop 클래스는 다음과 같은 클래스 변수를 가지고있습니다.
total은 전체 매출액을 의미하고 menu_list의 각 요소는 {메뉴명: 가격}으로 구성된
딕셔너리 입니다.
total = 0
menu_list = [{'떡볶이': 3000}, {'순대':3000}, {'튀김':500}, {'김밥':2000}]

- 매출이 생기면 다음과 같은 방식으로 메뉴와 판매량을 작성합니다.
Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

- 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f'매출: {Shop.total}원')

[ 출력 ]
매출: 9500원
'''
class Shop:

    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls, menu, count):
        for v in cls.menu_list:
            for k in v:
                if menu == k:
                    cls.total += v[menu] * count

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print(f'매출: {Shop.total}원')

'''
3. 다음 지시사항을 읽고 Hybrid 클래스를 구현하세요.

[ 지시 사항 ]
- 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현하세요.
class Car:
    
    max_oil = 50 # 최대 주유량
    
    def __init__(self, oil):
        self.oil = oil
    
    def add_oil(self, oil):
        if oil <= 0: # 0이하의 주유는 X
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil
            
    def car_info(self):
        print(f'현재 주유 상태: {self.oil}')
- 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
    ㄴ 최대 배터리 충전량은 30입니다.
    ㄴ 배터리 충전하는 charge() 메소드가 있습니다.
        - 최대 충전량을 초과하도록 충전할 수 없고, 0보다 작은 값으로 
            충전을 할 수 없습니다.
    ㄴ 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메소드가 있습니다.
    
[ 동작 ]
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

[ 출력 ]
현재 주유 상태: 50
현재 충전 상태: 30
'''
class Car:
    
    # 최대 주유량
    max_oil = 50

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유 상태: {self.oil}')

class Hybrid(Car):

    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil)
        self.battery = battery

    def charge(self, battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
                self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전 상태: {self.battery}')

car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

