"""
파일 : day12-02-class_init_del
개요 : 생성자, 소멸자
page : 274 ~ 277
"""

'''
1. 생성자

[ 생성자 사용 이전 ]
- 인스턴스 변수를 인스턴스 메소드를 통해서 생성하고있었음.
* 값을 저장하는 인스턴스 메소드를 나중에 호출하기 때문에.
문제가 발생할 수 있음.
[ 생성자 사용 후 ]
- 해당 클래스가 객체로 생성될때 미리 인스턴스 변수를 만들어줌.
->> 생성자가 해줌.

* 생성자는 객체를 생성할 때 자동으로 호출되는 메소드입니다.
-> 이미 Python에서 만들어줌.
class A:
    pass

print(dir(A))

* __두개가 들어가있는 메소드들은 파이썬에서 미리 기능과 역할이 부여된
메소드다.

[ 생성자의 구조 ]
def __init__(self, 매개 변수):
    인스턴스 변수 선언
'''

# [ 생성자 사용 전 ]
# class Candy:
#
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
# satang = Candy()
# satang.set_info('circle', 'brown')

# [ 생성자 사용 후 ]
class Candy:

    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

satang = Candy('circle', 'brown')

'''
2. 소멸자
인스턴스가 생성될때 => 생성자 호출
인스턴스가 소멸될때 => 소멸자 호출

[ 소멸자 구조 ]
def __del__(self):
    인스턴스 소멸시 동작할 코드
'''
class Sample:

    def __del__(self):
        print('인스턴스가 소멸됩니다....')

sample = Sample()
del sample

'''
책 예제 2번 ) 다음은 생성자와 소멸자를 이용해서 
서비스 안내 메시지를 출력하는 프로그램입니다.

[ 지시 사항 ]
- Service 클래스를 만드세요.
- 생성될때 어떤 서비스를 위한 클래스인지 전달하고 해당 서비스에 대한 출력을 띄우세요.
- Service 클래스가 제거되면 해당 서비스가 종료되었다고 출력해주세요.

[ 출력 ]
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''
class Service:

    # 생성자
    def __init__(self, service):
        self.service = service
        print(f'{self.service} Service가 시작되었습니다.')

    # 소멸자
    def __del__(self):
        print(f'{self.service} Service가 소멸되었습니다.')

s = Service('길 안내')
del s


