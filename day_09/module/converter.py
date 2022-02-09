"""
파일 : converter
개요 : 모듈의 생성
- 모듈을 직접 만들어본다.
"""

'''
함수 4개를 만든다.
1. str_to_int() : 문자열(여러개) -> 정수(list)로 변환해주는 함수 
2. int_to_str() : 정수(여러개) -> 문자열(list)로 변환해주는 함수 
3. float_to_str() : 실수(여러개) -> 문자열(list)로 변환해주는 함수
4. str_to_float() : 문자열(여러개) -> 실수(list)로 변환해주는 함수 

** 모든 함수의 인수는 *(애스터 리스크)를 사용합니다.
** 모든 함수의 반환 값은 List 값 
'''

# 1. str_to_int()
def str_to_int(*args):
    """
    문자열로 전달 받은 인수들을 모두 정수 형태로 변경 해주는 함수
    :param args: 문자열 인수
    :return: list[int(args)]
    """
    # 4줄이 -> 1줄로 줄일 수 있다.
    # 리스트 내포 ( 121p )
    # li = []
    #
    # for arg in args:
    #     li.append(int(arg))
    #
    # return li
    return [int(arg) for arg in args]

# print(str_to_int('1', '2', '3'))

# 2. int_to_str
def int_to_str(*nums):
    """
    정수로 전달 받은 인수들을 모두~~ 문자열 타입으로 변경 해주는 함수
    :param nums: 정수 인수
    :return: list[str(nums)]
    """
    return [str(num) for num in nums]

# 3. float_to_str
def float_to_str(*flts):
    """
    실수로 전달 받은 인수들을 모두 문자열 타입으로 변경 해주는 함수
    :param flts: 실수 인수
    :return: list[str(flts)]
    """
    return [str(flt) for flt in flts]

# 4. str_to_float
def str_to_float(*args):
    """
    문자열로 전달 받은 인수들을 모두 실수형 타입으로 변경을 해주는 함수
    :param args: 문자열 인수
    :return: list[str()]
    """
    li = []

    for arg in args:
        li.append(float(arg))

    return li












