"""
개요 : 출력
"""

'''
print({}) : '{}' 안에 있는 무언가를 출력해준다. 
'{}' 아무것도 넣지않으면 줄바꿈 처리 
'''

print()
print(10)
print()
print(20)

'''
\n, \t, \\, \'
'''
# <br> = \n
print("가\n나\n다")
print("이름\t나이")
print("가\t10")
print("Hello \"World")
print("Hello 'World")

a = 10
b = 20
c = 30
# 10 20 30
print(a)
print(b)
print(c)

print(a, b, c)
# 10 + 20 + 30
print(a, b, c, sep=" + ")

'''
python
1. all 
    1-1. %d : 정수 
    1-2. %s : 문자열
    1-3. %f : 실수 
'''
# all
# %d, %s, %f
a = 10
b = "가"
c = 10.1
# 10 + 가 = 10.1
print('%d + %s = %.1f' % (a, b, c))


# python 2.x
'''
{}
자료형을 선언해줄 필요가 없다.  
'''

print('{} + {} = {}'.format(a, b, c))

# python 3.x
'''
f'{}'
'''
print(f'{a} + {b} = {c}')




