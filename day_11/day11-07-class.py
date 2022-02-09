"""
파일 : day11-07-class
개요 : 클래스의 구성
page : 264 ~ 269
"""

'''
1. 클래스의 기본 구성
객체를 만들어내는 클래스는 객체가 가져야 할 구성요소를 
고스란히 가지고있습니다.

객체를 생성하기 위해서 클래스는 객체가 가져야 할 값과 기능을 가지고있어야합니다.

예시 ) 사람
값 - 이름, 나이, 연락처, 주소 등
기능 - 잔다, 먹는다, 공부한다, 달린다 등 

각각을 다음과 같이 생각하면됩니다.
값 = 변수
기능 = 함수

즉, 클래스는 변수와 함수로 구성되어있다고 생각하면됨.

- 클래스를 구성하는 변수는 2가지로 분리
1. 클래스 변수
    - 클래스를 기반으로 생성된 모든 객체가 공유하는 변수
    - 해당 클래스로 만들었다면 모두 공유하는 변수
2. 인스턴스 변수
    - 각각 객체마다 다르게 가지고있는 변수
    
- 클래스를 구성하는 함수(메소드)는 3가지로 분리
1. 클래스 메소드
2. 정적 메소드
3. 인스턴스 메소드
'''

'''
2. 인스턴스 변수와 인스턴스 메소드
2.1 - 인스턴스 변수
        - 객체들이 각각 따로 저장하는 변수
        - self 키워드를 앞에 붙여서 사용
2.2 - 인스턴스 메소드
        - 인스턴스 변수를 사용하는 메소드
        - 각 객체마다 다른 값으로 동작하는 메소드
        - 반드시 첫 번째 매개변수로 self를 추가해야함.
'''

# 인스턴스 변수와 인스턴스 메소드를 가지는 Person 클래스 구현
class Person:

    def who_am_i(self, name, age, tel, address):
        """
        - 인스턴스 메소드
            - 첫 번째 매개 변수가 self == 인스턴스 메소드
            - 모든 객체는 who_am_i() 메소드를 호출 할 수 있음.
            - self에는 who_am_i() 메소드를 호출하는 인스턴스가 전달
            - self를 제외한 나머지 매개변수에 실제로 사용될 데이터 전달
        """
        # 인스턴스 변수 name에 매개변수 name값을 정의
        self.name = name
        # 인스턴스 변수 age에 매개변수 age값을 정의
        self.age = age
        # 인스턴스 변수 tel에 매개변수 tel값을 정의
        self.tel = tel
        # 인스턴스 변수 address에 매개변수 address값을 정의
        self.address = address

boy = Person()
boy.who_am_i('john', 15, '123-1234', 'toronto')
# 인스턴스 메소드의 self 는 boy라고 생각하면 편합니다.
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

# 해당 객체로 사용할 수 있는 메소드, 변수를 보여줌
print(dir(boy))

'''
책 기본예제 ) CPU, RAM, VGA, SSD를 구성요소로 가지고있는 Computer 클래스를
이용해서 인스턴스를 생성하는 프로그램입니다.
조건을 참고하여 클래스를 만들어보세요.

[ 조건 ] 
- 각 구성요소를 저장할 수 있는 메소드 set_spec() 메소드를 가지고있어야함.
- 구성요소를 출력할 수 있는 hardware_info() 메소드를 가지고있어야함.

[ 출력 ]
CPU=i7
RAM=16GB
VGA=GTX1060
SSD=512GB
CPU=i5
RAM=8GB
VGA=MX300
SSD=256GB
'''
# CPU, RAM, VGA, SSD
class Computer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU={self.cpu}')
        print(f'RAM={self.ram}')
        print(f'VGA={self.vga}')
        print(f'SSD={self.ssd}')


computer1 = Computer()
computer1.set_spec('i7','16GB','GTX1060','512GB')
computer2 = Computer()
computer2.set_spec('i5','8GB','MX300','256GB')

computer1.hardware_info()
computer2.hardware_info()

# 기본 예제 2번은 eval() 함수를 이용할 뿐 인스턴스 메소드와 인스턴스 변수를 잘 활용하는 것 
