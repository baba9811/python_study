"""
파일명 : module3
*( 애스터리스크 )를 사용한 from 절을 사용해보자.
"""
# from converter import int_to_str
# from converter import float_to_str
# ctrl + ? : 드래그된 영역 모두 주석

from converter import *
# * == 모두 전체

print(int_to_str(1, 2, 3, 4, 5))
print(float_to_str(1.0, 2.0, 3.0, 4.0))

# 애스터 리스트(*)를 사용하면 함수를 호출 할 때마다 모듈을 명시할 필요가 없습니다.

