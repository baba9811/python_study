"""
개요 : 기본 자료형 ( int, float, str, bool )
"""

'''
int - 정수 [ Integer ]
파이선 2.x int, long 
int = xxxxx + 1 -> Error 
long = xxxxx + 1 -> o
Java 
int, byte, long ...

숫자 2를 저장할려고하는데 
메모리에 int 만큼의 범위를 지정을해야되나?
메모리는 [ xxxxx ] 공간을 할당 받고 2 를 여기에 저장함 ( 비효율 )
 
파이선 3.x 
int 

str -> int -> float 등 변경 가능
int({}) : '{}' 안에있는 어떠한 값을 int 로 변경한다 

# 어떤 자료형인지 알고싶을때
type({})을 사용 : '{}' 안에있는 값의 자료형을 알려준다.
'''

a = "100"
b = int(a)

print(b)
print(type(b))

'''
float - 실수 [ floating point number ]

float({}) : '{}' 안에 있는 무언가의 값을 실수형으로 변경 
'''

a = 10
print(float(a))

b = "100"
c = int(b)
d = float(c)

print(d)

'''
str - 문자열 [ String ]
 
str({}) : '{}'안에 들어오는 무언가를 문자열로 변경할 수 있다.
'''

a = 100
d = str(a)

print(d)

'''
문자 인덱싱 

100 -> "100" 
[ '1', '0', '0' ]
   0    1    2  .....
   
'''
d = "abcd"
# "abcd" = [ 'a', 'b', 'c', 'd' ]
print(d[1])

'''
문자열 슬라이싱
s[start:end:step]
end는 주어진 숫자 사이 값을 보여주는거에요
end = start + 내가 보고싶은 문자열의 갯수
        1   +  2 = 3
'''
d = "abcdfg"
print(d[1:3])
# step - n개씩 점프
# abcdfg - b c d 'f'

'''
bool - 논리 [ boolean ]
True, False ( 참, 거짓 )

( 조건문 )
bool({}) : {} 안에있는 무언가를 논리값으로 변경함  
Java 
true, false 
python 
True, False 
'''

# False ( 거짓 )
# 1. 0
print(bool(0))
# 2. None != 0
print(bool(None))
# 3. []
print(bool([]))
# 4. ''
print(bool(''))

'''
예제 1)
다음과 같은 학생 정보가 있다. 이 정보를 이용해서 변수를 만들어보자.
1. 이름 : 'Alice'
2. 나이 : 20
3. 남자친구 : 없다.... ㅠ_ㅠ
4. 키 : 170.2
'''

name = 'Alice'      # 문자열
age = 20            # 정수
boyfriend = False   # 논리
tall = 170.2        # 실수

