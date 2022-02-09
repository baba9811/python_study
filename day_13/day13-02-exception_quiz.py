"""
파일 : day13-02-exception_quiz
개요 : 응용문제
page : 306 ~ 309
"""

'''
1. 다음 지시사항을 읽고 우리나라의 모든 도를 맞히는 퀴즈를 진행할 수 있는 Quiz 클래스를
구현하세요.

[ 지시사항 ]
- Quiz 클래스는 다음과 같은 클래스 변수를 가지고있습니다.
answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도',
'경상남도', '경상북도', '제주틀별자치도' ]
- challenge() 메소드는 사용자의 입력을 처리하고 일치하는 정답이 있으면 '정답입니다'를
출력한 뒤, 해당 정답을 answer에서 제거합니다. 그리고 다시 challenge() 메소드를 호출합니다.
- challenge() 메소드는 사용자의 입력이 틀린 경우 '틀렸습니다'라는 예외 메시지를 출력할 수 
있도록 예외를 발생시킵니다.
- Quiz 클래스의 동작 확인은 다음과 같은 코드로 진행합니다.
try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challenge()
except Exception as e:
    print(e)
- 정답을 맞히면 다음과 같은 메시지를 출력합니다.

[ 출력 ]
우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.
정답은? >>> 경기도
정답입니다.
정답은? >>> 울룽도
틀렸습니다.
'''

# class WrongAnswer(Exception):
#
#     def __init__(self):
#         super().__init__('틀렸습니다')


# class Quiz:
#     # 클래스 변수 선언
#     answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도',
#               '전라북도','경상남도', '경상북도', '제주특별자치도']
#
#     @classmethod
#     def challenge(cls):
#         area = input('정답은? >>> ')
#         for i, v in enumerate(cls.answer):
#             if v == area:
#                 print('정답입니다.')
#                 cls.answer.pop(i)
#                 # 재귀 함수
#                 # 재귀 함수는 조건문이 필수
#                 cls.challenge()
#                 # return 을 사용한 이유는 완전히 종료되지 않았을 것 같은
#                 # 메소드를 없애기위함
#                 return
#         raise WrongAnswer()
#
# try:
#     print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
#     Quiz.challenge()
# except Exception as e:
#     print(e)

'''
2. 다음 지시사항을 읽고 컴퓨터가 생성한 난수를 맞히는 UpDonw 게임을 실행하는 UpDown 클래스를
구현하세요.

[ 지시사항 ]
- UpDown 클래스의 인스턴스를 생성하면 1~100 사이의 난수가 인스턴스 변수 answer에 저장됩니다.
인스턴스 생성 후에는 play() 메소드만 호출합니다.
game = UpDown()
game.play()
- challenge() 메소드는 사용자의 입력을 처리합니다.
유효하지 않은 정수값을 입력하면 예외를 발생시키고 '1~100 사이만 입력하세요' 라는 예외 메시지를
출력합니다.
- challenge() 메소드가 호출될 때마다 인스턴스 변수 count가 1씩 증가합니다.
최종적으로 count 변숫값으로 몇번의 시도 끝에 성공했는지 알 수 있습니다.
- 생성된 난수를 맞히기 전에는 프로그램이 종료되지 않습니다.
- 정수 대신 다른 자료형의 값은 입력되지 않는다고 가정합니다.

[ 출력 ]
입력(1~100) >>> 200
1~100 사이만 입력하세요.
입력(1~100) >>> 50
Down!
입력(1~100) >>> 35
3번만의 정답입니다.
'''

# import random
#
# class OverRangeValueError(Exception):
#
#     def __init__(self):
#         super().__init__('1~100 사이만 입력하세요')
#
#
# class UpDown:
#
#     def __init__(self):
#         self.answer = random.randint(1, 100)
#         self.count = 0
#
#     def challenge(self):
#         try:
#             input_answer = int(input('입력(1~100) >>> '))
#             if input_answer > 100 or input_answer < 1:
#                 self.count += 1
#                 raise OverRangeValueError()
#             elif input_answer > self.answer:
#                 self.count += 1
#                 print('Down!')
#                 self.challenge()
#             elif input_answer < self.answer:
#                 self.count += 1
#                 print('Up!')
#                 self.challenge()
#             elif input_answer == self.answer:
#                 self.count += 1
#                 print(f'{self.count}번 만의 정답입니다.')
#         except OverRangeValueError as e:
#             print(e)
#             self.challenge()
#
#     def play(self):
#         self.challenge()
#
# game = UpDown()
# game.play()

'''
3. 다음 지시사항을 읽고 입금, 출금, 이체, 조회 기능이 있는 BankAccount 클래스를 구현하고,
추가로 예외 사항을 처리할 수 있는 BankError 예외 클래스를 구현하세요.

[ 지시 사항 ]
- BankAccount 클래스
    { 인스턴스 변수 }
    - 계좌번호: acc_no
    - 통장 잔액: balance
    { 생성자 }
    - 매개변수: acc_no, balance
    { 입금 기능 }
    - 메소드명 : deposit
    - 매개변수 : money # 입금할 금액
    - 반환값 : 없음
    - 예외사항 : 0원 이하로 입금하려고 할때
    { 출금 기능 }
    - 메소드명: withdraw
    - 매개변수: money # 출금할 금액
    - 반환값: 실제로 출금된 금액
    - 예외 사항: 0원 이하로 출금할때, 통장 잔액보다 큰 금액을 출금하려고 할때 
    { 이체 기능 }
    - 메소드명: transfer
    - 매개변수 :your_acc, money # 상대방 계좌, 이체할 금액
    - 반환값 : 없음
    { 조회 기능 }
    - 메소드명 : inquiry
    - 매개변수 : 없음
    - 반환값 : 없음
    - 기능: 계좌 번호와 통장 잔액을 화면에 출력
[ 예외 사항 ]
1. 마이너스 금액 입금
me = BankAccount('012-34-56789', 50000)

try:
    me.deposit(-1000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
{출력}
-1000원 입금 불가
계좌번호: 012-34-56789
통장 잔액: 50000원
** 나머지 예외사항은 책 참고
[ 정상 상황 ]
me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)

try:
    me.transfer(you, 5000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
    you.inqury()
{ 출력 }
계좌번호 : 012-34-56789
통장잔액: 45000원
계좌번호 : 987-65-43210
통장잔액: 55000원
'''

class BankError(Exception):

    def __init__(self, msg):
        super().__init__(msg)

class BankAccount:

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, money):
        """
        입금 기능
        """
        if money <= 0:
            raise BankError(f'{money}원 입금 불가')
        else:
            self.balance += money
    
    def withdraw(self, money):
        """
        출금 기능
        """
        if money <= 0:
            raise BankError(f'{money}원 출금 불가')
        elif money > self.balance:
            raise BankError('잔액 부족')
        else:
            self.balance -= money
            return money

    def transfer(self, your_acc, money):
        """
        이체 기능
        """
        self.balance -= money
        your_acc.balance += money

    def inquiry(self):
        """
        출력 기능
        """
        print(f'계좌번호: {self.acc_no}')
        print(f'통장 잔액: {self.balance}')

me = BankAccount('012-34-56789', 50000)

try:
    me.deposit(-1000)
except BankError as e:
    print(e)
finally:
    me.inquiry()

me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)

try:
    me.transfer(you, 5000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
    you.inquiry()

# 검색 및 공부 트랜잭션
