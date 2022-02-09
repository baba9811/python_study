"""
파일명 : module2
converter 모듈을 import 시켜서 해당 모듈에 있는 함수 사용!
* from 모듈 import 함수
"""
from converter import int_to_str
from converter import float_to_str

print(int_to_str(1, 2, 3, 4, 5))
print(float_to_str(1.0, 2.0, 3.0, 4.0))

'''
from을 사용하면 함수를 호출하는 방법을 유심하게 볼 필요가 있다 !!!!
import 만 사용했을때는 
모듈.함수명() 이렇게 사용을 했으나.
from import를 사용하면 
함수명()만 사용해도 되는 것을 확인 할 수 있다.
'''









