"""
파일 : day12-03-inheritance
개요 : 상속
page : 283 ~ 286
"""

'''
1. 상속 ?
- 파이썬 기준
어떤 클래스가 가지고 있는 기능을 그대로~~ 물려받아서 사용할 수 있는
클래스를 만든다.

다른 클래스의 기능을 물려받을 때 상속받는다는 표현을 사용

-> 상속 관계에 있는 클래스를 표현할 때
부모 클래스, 자식 클래스 용어 사용

[ 관계도 ]
부모 클래스(상속해주는 클래스) ----> 자식 클래스(상속받는 클래스)

[ 용어 ]
부모 클래스 = 슈퍼 클래스 = 기반 클래스

자식 클래스 = 서브 클래스 = 파생 클래스

* 파이썬에서 super라는 키워드를 사용하여 부모 클래스를 지정하므로.
이에따라 저희도 다음과 같이 용어를 사용할것.
부모 클래스 -> 슈퍼 클래스
자식 클래스 -> 서브 클래스
'''

'''
2. 상속 관계 구현

[ 조건 ] 
- 두 클래스가 IS-A 관계를 성립해야함.
    - IS-A == '~은 ~이다.'
    ex) 학생'은' 사람'이다' ==> 'Student' is a 'Person'
    = Student == 서브 클래스
    = Person == 슈퍼 클래스
    
[ 사용법 ]
- 슈퍼 클래스는 일반 클래스처럼 구현.
- 서브 클래스는 어떤 클래스를 상속받고있는지 명시 

[ 형식 ]
- 슈퍼 클래스 
class 슈퍼 클래스:
    본문

- 서브 클래스
class 서브 클래스(슈퍼 클래스):
    본문

* 서브 클래스를 구현할때는 괄호 안에 어떤 슈퍼 클래스를 상속받았는지 명시!!
* 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용 가능
'''

# 슈퍼 클래스
class Person:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}가 {food}를 먹습니다.')

# 서브 클래스
class Student(Person):

    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f'{self.name}는 {self.school}에서 공부를 합니다.')

potter = Student('해리포터', '호그와트')
potter.eat('감자')
potter.study()

'''
Person은 슈퍼 클래스입니다.
name을 전달해서 생성할 수 있으며, eat() 메소드를 가지고있습니다.

Student는 서브 클래스입니다.
name과 school을 전달해서 생성할 수 있으며 study() 메소드를 가지고있습니다.

Student는 Person 슈퍼 클래스를 상속받았기 때문에
Person 클래스의 eat() 메소드도 사용할 수 있습니다.

** 여기서 중요한것 
-> Student 클래스의 생성자가 중요함.
'''

'''
뭣이 중한디??
3. 서브 클래스의 __init__()
- 서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없음.
- 부모가 존재해야 자식도 존재할 수 있다.
- 이와 같이 서브 클래스의 생성자를 구현할 때는 반드시 슈퍼 클래스의 생성자를 
먼저 호출해야함
- super 키워드를 사용 ( 슈퍼 클래스를 의미 )
'''

'''
4. 서브 클래스의 인스턴스 자료형
슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스입니다.
그에 비해 서브 클래스 객체는 서브 클래스의 인스턴스 이면서
동시에 슈퍼클래스의 인스턴스입니다.
-> Student Object == Person Object

- 어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 
isinstance() 함수를 사용함.

[ 사용법 ]
isinstance(객체, 클래스)

[ 반환값 ]
True or False
'''

print(isinstance(potter, Student))
print(isinstance(potter, Person))

'''
책 예제 ) 원두를 저장하는 Coffee 클래스와 원두에 물을 섞은 Espresso 클래스를
상속 관계로 구현해보자.
'''
class Coffee:

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print(f'원두 {self.bean}')

class Espresso(Coffee):

    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f'물 {self.water}ml')

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()














