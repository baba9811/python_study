"""
파일 : day04-04-loop1
개요 : 반복문, while
책 : 102 ~ 113
"""

'''
반복문은 어떤 수행 작업을 한 번이 아니라 계속 수행해야 할 때 사용합니다.
'다람쥐 쳇바퀴 돌듯'이라는 말처럼 계속해서 수행해야 하는 프로그램이 필요할 때
반복문을 사용합니다.

하루 일상이 반복되고, 사계절 반복되듯 반복문은 우리의 주변에 매우 가까이 있으며
프로그래밍을 할 떄도 자주 사용됩니다.

python에서 반복문은 두개로 나누어집니다.
1. while
2. for

* '상황'에 따라 두 반복문을 적정히 선택하여 처리하는 것이 중요함.
'''

'''
1. while 문
while문은 (특정 조건)을 만족하는 동안은 계속 수행해야 하는 코드를 작성할 때 사용합니다.

while문의 기본 구조는 다음과 같습니다.

while (조건식):
    반복할 실행문
    
* 들여쓰기는 필수!!!!!!

조건식의 결과가 True이면 반복 실행문을 실행합니다.
반복할 실행문을 한 번 실행하면 다시 조건식으로 이동하여 조건식 결과를 판단 후,
결과의 상태에 따라 다시 반복할 실행문을 실행하거나 반복문을 종료하게됩니다.

# 순서도 
'''

# while True:
#    print('Hello Python')

'''
무한 루프
무한 루프 중지 방법은 IDE 에서는 중지 버튼을 누르거나 ctrl + c를 이용하면됩니다.
ctrl + c = cmd, linux(shell)
'''

'''
while 문의 조건식을 True로 지정하게 되는 경우는 보는 바와 같이 계속 반복 된다.
이를 '무한 루프'라고 하며 얼핏보면 많이 사용 안 할것 같지만.
나중에 나오는 break를 이용해 원하는 시점에 언제든 종료가 가능해서 
무한 루프 식을 자주 사용합니다.
'''

# while True:
#     print('Hello World')
#     break

# 예제 ) 1 ~ 10까지 출력하기

# num = 1
# while num <= 10:
#     print(num)
#     num += 1
#
# # 책 예제 ) 1부터 10사이의 모든 정수를 '역순'으로 출력해보세요
#
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1 # = num = num - 1 ( -=, +=, *= .. )

# 예제 ) Hello Python라는 문자열이있는데 다음과같이 출력해보세요.
'''
Hello Python
Hello Pytho
Hello Pyt
.
.
.
H
'''

# s = 'Hello Python'
# index = len(s)
# # True, False False = '', [], None, 0
# while s:
#     print(s)
#     index -= 1
#     s = s[:index]

'''
2. while문이 필요한 경우

이번에는 while문으로 반복해서 처리해야 할 작업 범위가 명확하지 않은 경우를 살펴보겠습니다.
지금까지는 'Hello Python' 처럼 반복해서 처리해야 할 값의 범위가 정해져 있었으나.
언제나 이처럼 명확하게 범위가 제공되는 않습니다.

예시) 월급을 기다리고있는 회사원이 1분마다 은행어플켜서 통장을 확인하고 있다면 
다음과 같은 반복문이 만들어집니다.

while 돈 입금 완료 여부:
    통장 잔고 확인
    1분 대기
    if 돈 입금 완료:
        돈 입금 완료 여부 = False

'''
'''
책 예제 ) 사용자로부터 임의의 정수를 입력받아 모두 리스트([])에 보관합니다.
단, 사용자가 0을 입력하면 더 이상 입력받지 않고 프로그램을 종료합니다.
이때!!! 0은 리스트에 보관하지 않습니다.
'''

# my_list = []
# bol = True
#
# while bol:
#     n = int(input('정수를 입력하세요(종료는 0입니다). >>>'))
#     if n == 0:
#         bol = False
#     else:
#         my_list.append(n)
#
# print(my_list)

'''
3. while문의 중첩
while문 내부에 또 다른 while 문이 나타나는 것을 while문의 중첩이라고 합니다.
반복 처리해야 하는 대상이 2개 이상이면 while 문의 중첩이 필요합니다.

반복 처리할 대상이 2개면 while 문이 2개 필요합니다.
반복 처리할 대상이 3개면 while 문이 3개 필요합니다.
반복 처리할 대상이 4개면 while 문이 4개 필요합니다.
...

* while문이 많이지면 많아질 수록 복잡하기 때문에 대부분 2~3개만 사용합니다.
'''

'''
책 예시 ) 총 5일 동안 매일 3시간씩 수업을 진행합니다. 매 시간 '1일차 1교시입니다.'
와 같은 메시지를 출력해야 합니다.
1일차부터 5일차까지 반복되는 일수와 1교시부터 3교시까지 반복되는 시간이라는 
2개의 반복 처리 대상이 있으니 while문의 중첩이 필요합니다.

1 2 3 4 5 일
1 2 3
1 2 3
1 2 3... 5일
'''
# 일
day = 1

while day <= 5:
    hour = 1
    while hour <= 3:
        print(f'{day}일차 {hour} 교시입니다.')
        hour += 1
    day += 1

'''
예제 ) 1 ~ 9 단까지 구구단을 만들어보세요. 출력은 다음과 같아야합니다.
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3 
.
.
.
9 x 9 = 81
'''

dan = 1
while dan <= 9:
    n = 1
    while n <= 9:
        print(f'{dan} x {n} = {(dan * n)}')
        n += 1
    dan += 1

'''
# 책 예제 ) 정수를 입력받아서 그 횟수만큼 'Hello'를 출력하는 프로그램을 구현하세요.
# 0 이하의 값이 입력되면 '잘못된 입력입니다'라는 오류 메시지를 출력하세요.
'''

num = int(input('정수를 입력하세요 >>>'))

if num > 0:
    index = 1
    while num != 0:
        print(f'{index}번째 Hello')
        index += 1
        num -= 1
else:
    print('잘못된 입력입니다.')










