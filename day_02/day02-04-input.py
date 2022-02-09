"""
day02-04-input
개요 : 입력
"""

'''
a = 10
b = 20 
'''

# num = input()
# print(f'{num}')

# num2 = input('아무거나 입력해주세요 :')
# print(f'{num2}')

'''
input 입력 받았을때 항상 str 반환 
'''

'''
예제 1. 
정수를 입력받아서 int 형으로 변경해주세요 ( type ) 
'''

# num = input('정수를 입력해주세요: ')
# num = int(num)
# print(type(num))

'''
예제 2)
무언가를 입력받아서 (bool)True, (bool)False 한개씩 띄워보기 
'''

#s = input('아무거나 입력해주세요 : ')
# str '0'  0 x
#print(bool(s))

a = input('아무거나 입력해주세요:')
a = int(a)
print(bool(a))