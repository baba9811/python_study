"""
파일명 : day08-03-argument_parameter
개요 : 인수와 매개변수
page : 188 ~ 191
"""

'''
함수로 전달되는 인수(argument)를 저장하는 변수를 매개변수(parameter)라고 합니다.
이 둘은 다른 개념이지만 함수가 호출된 뒤에는 인수와 매개변수가 같은 값을 가지게 되므로
이를 구분하지 않고 부르는 경우가 있습니다. 

def welcome(매개변수):
    print(매개변수)

인수 = 1
welcome(인수)
'''

'''
1. 인수가 있는 함수
'''
#
# def introduce(name, age): # 2
#     print(f'내 이름은{name}이고, 나이는 {age}살 입니다') # 3
#
# introduce('james', 25) # 1

# 인수는 넘겨줄때 매개변수가 넘겨준 순서대로 저장됨.

'''
예제 ) 점수를 입력하면 해당 점수가 출력되는 함수를 만드세요
함수명 : show()
'''

# def show(score):
#     print(f'{score}')
#
# show(80)

'''
예제 ) 점수를 10개 입력하면 해당 점수들이 출력되는 함수를 만드세요.
함수명 : show_ten()
# 함수 1번호출 or 10번호출 
'''

# def show_ten(score):
#     print(f'{score}')
# for i in range(10):
#     show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))
# show_ten(int(input('점수를 입력하세요 >>>')))

# def show_ten(scores):
#     for i in scores:
#         print(f'{i}')
#
# li = []
# for i in range(10):
#     li.append(int(input('점수를 입력하세요 >>>')))
#
# show_ten(li)

'''
2. 가변 매개변수
함수로 전달해야 하는 인수의 개수가 정해지지 않아도
매개변수를 선언할 수 있습니다. 
이를 가변 매개변수라고 합니다. 
가변 매개변수를 만드는 키워드는 애스터리스트(*)입니다.
매개변수 앞에 *를 붙이면
곧바로 가변 매개변수가 되면서 전달되는 모든 인수를 하나의 튜플로 만들어줍니다.

* show() 함수를 만든다. 
- show()함수는 전달받은 모든 인수를 하나씩 출력하는 함수.
'''

'''
예제 ) 함수를 두개 만드는데 하나는 인수가 하나인 값만 받아서 출력
두번째 함수는 두개의 인수를 받아서 두개의 인수를 출력
함수 명 : one(인수), two(인수1, 인수2)
호출 출력
one(1)
1
two(1, 2)
1
2
'''

# def one(num):
#     print(num)
#
# def two(num1, num2):
#     print(num1)
#     print(num2)
#
# one(1)
# two(1, 2)

# def three(*nums):
#     for i in nums:
#         print(i)

def show(*args):
    print(args)
    for item in args:
        print(item)

show('python')
show('happy', 'birthday')

'''
3. 디폴트 매개변수
매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용할 수 있도록 
매개변수에 기본값을 설정할 수 있습니다.
이 것을 디폴트 매개변수(기본 매개변수)라고 합니다.
* greet() 함수를 만들어서 실험해보자.
- 사용자가 함수를 호출할때 매개변수로 아무 값도 넣지 않는다면 
'안녕하세요'라는 인사말이 화면에 나타난다.
'''

# 매개변수에 아무 값이 들어오지 않을때 '안녕하세요'를 출력
def greet(message='안녕하세요'):
    print(message)

greet()
# 매개변수로 반갑습니다가 들어가서 반갑습니다 출력됩니다.
greet('반갑습니다.')

# def greet(message='안녕하세요', name):
#     print(f'{name}님, {message}')
#
# greet('김철수')

'''
non-default argument follows default argument
- 기본 인수가 아닌 인수가 기본 인수를 따르고있다.
-> 기본 인수가 아닌 인수가 기본 인수 뒤에 위치하고있다.
'''

def greet(name, message="안녕하세요"):
    print(f'{name}님, {message}')

greet('김철수')
'''
디폴트 값을 가지는 매개변수 message를 뒤에 배치하면 '김철수'는 name에 저장되고
message는 디폴트 값을 사용합니다.
**** 항상 디폴트 값을 가지는 매개변수는 뒤에 배치하는 게 좋습니다.
'''

'''
디폴트 매개변수 사용 잘 안할 것 같다?
- 실제로는 사용 많이함.
print()
1. 호출할때 편하다(?) 짧아진다
2. 중복코드 제거가능
'''

# def welcome(message='안녕하세요'):
#     print(message)
#
# welcome()
# welcome()
# welcome()
# welcome()
# welcome()
# welcome()
# welcome('어서오세요')
# welcome()
# welcome()
# welcome()

'''
책 예제 ) 다음은 전달된 모든 인수를 모두 더해서 합계를 출력한 프로그램입니다.
함수명 - adder()
(1, 2)의 합은 3입니다.
(1, 2, 3)의 합은 6입니다.
(1, 2, 3, 4)의 합은 10입니다.
'''

# def adder(*nums):
#     print(f'{nums}의 합은 {sum(nums)}입니다.')
#
# adder(1, 2)
# adder(1, 2, 3)
# adder(1, 2, 3, 4)




