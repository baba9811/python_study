"""
개요 : 연산자
"""

'''
연산자란?
특정한 작업을 수행하기 위해 사용하는 기호 

1. 산술 연산자 - 숫자 연산
2. 대입 연산자 - 대입 및 복합 대입
3. 관계 연산자 - 크기 비교
4. 논리 연산자 - 하나 이상의 논리적 처리
5. 비트 연산자 - 이진 연산
6. 기타 연산자 
'''

'''
1. 산술 연산자
    [ +, -, *, **, /, //, % ]
'''
num = 1
num2 = 2
print(num + num2)
print(num2 - num)
# x *
print(num * num2)

# num2 ** n = num2 n 번만큼 곱하는 것
# num2 * num2 * num2
print(num2 ** 3)

print(10/5)  # 실수 return
print(10//5) # 정수 return
# 3 / 2 (1)남는다
print(3%2)

'''
예제 ) (내가 숫자를 입력했는데 이놈이 짝수인지 홀수)인지 알려줘 !
'''

'''
num = input("숫자를 입력해주세요 : ")
num = int(num)
a = num % 2
# num % 2 = 0
# num % 2 = 0
# num % 2 = False
# False = 0, [], '' ,None
if num % 2:
    # True ( 0 != )
    print("Ture")
    print("홀수입니다")
else:
    # False ( 0 )
    print('False')
    print("짝수입니다.")
'''

'''
2. 대입 연산자 
    2.1 대입 연산
        - =
    2.2 복합 대입 연산자
        - +=, -=, *=, /=, //= ..  
'''
b = 10

# 복합 대입 연산자 **
s = "d"
s = "f"
s = "d"
# df
s = "d"
# add 'f'
# s += "f"
s = s + "f" # s = "d" + "f"
s = 10
s -= 2
# s += 1
print(s)
# /=, //=, *=, **=, %=

'''
예제 )
/=, //=, *=, **=, %= 한 번씩 이용해보기 

예제 ) 
숫자를 입력받으면 구구단 n x 1~9
 
n x 1 = 값
n x 2 = 값
n x 3 = 값
n x 4 = 값
n x 5 = 값
n x 6 = 값 
...
'''

'''
num = input("정수 입력해주세요:")
num = int(num)
print(f'{num} x 1 = {(num * 1)}')
print(f'{num} x 2 = {(num * 2)}')
print(f'{num} x 3 = {(num * 3)}')
print(f'{num} x 4 = {(num * 4)}')
print(f'{num} x 5 = {(num * 5)}')
print(f'{num} x 6 = {(num * 6)}')
print(f'{num} x 7 = {(num * 7)}')
print(f'{num} x 8 = {(num * 8)}')
print(f'{num} x 9 = {(num * 9)}')
'''

# = ( 등호 ) 같다 의미로 표현이되는데 프로그램
# == ( 수학적인 같다와 같다 )

'''
num = input("정수 입력해주세요:")
num = int(num)
for i in range(1, 10):
    print(f'{num} x {i} = {(num * i)}')
'''

# a = range(1, 10) = [0, 1, 2, ..., 9]

'''
3. 관계 연산자
    - >, >=, <, <=, ==, !=
'''
a = 10
b = 20
c = 10
print(a > b)  # a 가 b보다 크냐?
print(a >= b) # a 가 b보다 크거나 같냐?
print(a < b)    # b가 a보다 크냐?
print(a <= b)   # b가 a보다 크거나 같냐?
# >, < , <=, >=
# 변수 변하는 수
# 상수 - 변하지 않는 수
# a = 10
# PI = 3.14
# Java final ( 절대 변하지 않을때 )
# PI = 3.14
# final float PI = 3.14;
print(a == b) # a 와 b 가 같냐?
print(a != b) # a 와 b 가 같지 않냐?

for i in range(10): # 0 ~ 9
    if i != 0:
        print('찍는다!')

'''
4. 논리 연산자
    - and, or, not
'''
a = True
b = False

print(a and b) # a와 b가 둘다 True 일때 True 나머지는 다 False
print(a or b)  # a와 b가 둘다 False 일때 False 나머지는 다 True
print(not a)  # 반대로 변경 !!
print(a and not b)

'''
5. 비트 연산자 
    - &, |, ^, ~, <<, >>
    - & -> Shift + 7
    - | -> Shift + \
    - ^ -> Shift + 6
    - ~ -> Shift + ` (1 왼쪽)
    - <<, >> -> Shift + [',', '.']
'''

a = 13
b = 15
'''
CPU - 0, 1 [ 기계어 ] 
'''
print(bin(a)) # 0b1101

# - & 1 1 -> 1 이고 나머지는 0
print(bin(a), bin(b))
# 0b1101
# &
# 0b1111
# 0b1101
print(a & b)      # 10진법으로 보기
print(bin(a & b)) # 2진법으로 보기

# | : 둘다 0일때 0
# 0b1101
# |
# 0b1111
# 0b1111
print(a | b)
print(bin(a | b))

# ^ : a,b 0 : 0
#     a,b 1 : 0
# 0b1101
# |
# 0b1111

# 0b0010
# 0b10
print(a ^ b)
print(bin(a ^ b))

# ~ : 0 -> 1
#     1 -> 0
# 보수
# ~x = -x -1
print(~a)
print(bin(~a))

# << - a << n 2의 n 거듭제곱을 곱셈처리
# >> - b >> n 2의 n 거듭제곱을 나눗셈

print(a << 2) # 13 * 4(2 * 2)
print(a >> 2) # 13 / 4(2 * 2)

'''
6. 시퀀스 연산자
리스트, 튜플, range, 문자열등에 사용 되는 것입니다
 - * , + 
'''
a = "ab"
b = "cc"
print(a + b) # [ 'a', 'b' , 'c', 'c' ]
print(a * 2) # [ 'a', 'b' ] * 2

'''
7. 기타 연산자
리스트, 문자열, 딕셔너리 등에 무언가가 속해있는지 여부
    7.1 - 멤버십 연산자
        - in, not in 
    7.2 - 조건 연산자
        - [ True ] if [ 조건 ] else [ False ]
'''
b = "abcd"
print('b' in b)     # 'b'가 들어있냐?
print('b' not in b) # 'b'가 들어있지 않니?

# 조건 연산자
c = 1
print('True' if c == 1 else 'False')

if c == 1:
    print('True')
else:
    print('False')

'''
연산자의 우선순위 
연산자를 2개 이상 함께 사용할때 먼저 처리되는 연산자가 있습니다.
"어떤게 먼저 처리된다"
'''

print(1 + 2 * 3) # 3 * 3 | 2 * 3 + 1
print((1 + 2) * 3)

'''
예제 ) 정수를 입력 받고 2개의 값을 각각 더하기, 빼기, 나누기, 몫, 나머지, 곱셈
더하기 : {} 
빼기 : {}
나누기 : {}
몫 : {}
나머지 : {}
곱셈 : {}
'''

num = int(input("정수 1:"))
num2 = int(input("정수 2:"))
print(f"더하기 : {num + num2}")
print(f"빼기 : {num - num2}")
print(f"나누기 : {num / num2}")
print(f"몫 : {num // num2}")
print(f"나머지 : {num % num2}")
print(f"곱셈 : {num * num2}")