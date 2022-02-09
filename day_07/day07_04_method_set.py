"""
파일 : day07-04-method_set
개요 : set 메소드
page : 178 ~ 179
"""

'''
1. 교집합
두 집합에서 공통적인 요소만 추출하여 새로운 집합을 생성하는 집합 연산.
교집합은 & 또는 intersection() 메소드를 사용
& = shift + 7
'''
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2)
print(s1.intersection(s2))

'''
2. 합집합
두 집합의 모든 요소를 합친 새로운 집합을 생성하는 집합 연산입니다.
합집합은 | 연산자 또는 union() 메소드를 사용합니다.
| = shift + \
'''

s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 | s2)
print(s1.union(s2))

'''
3. 차집합
한 집합에서 다른 집합 요소를 뺀 새로운 집합을 생성하는 집합 연산.
차집합은 - 연산 또는 difference() 메소드를 사용합니다.
'''
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 - s2)
print(s1.difference(s2))













