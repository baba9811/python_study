"""
파일명 : module
- 'converter 모듈'을 'import' 시켜서 '해당 모듈'에 있는 함수 사용
** import
"""
import converter

# 1. str -> int
# f - function ( 함수 )
print(converter.str_to_int('1', '2', '3', '4'))

# 2. int -> str
print(converter.int_to_str(1, 2, 3, 4))

# 3. float -> str
print(converter.float_to_str(1.0, 1.2, 1.5, 1.7, 2.0))

# 4. str -> float
print(converter.str_to_float('1.0', '1.2', '1.5', '1.7', '2.0'))

# print(set(int_to_str(1, 2, 3, 4)))




