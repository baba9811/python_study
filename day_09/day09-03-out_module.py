"""
파일명 : day09-03-out_module
개요 : 외부 모듈
page : 219 ~ 220
"""

'''
1. 패키지
모듈의 상위 개념을 패키지(package) 라고 한다.
패키지란 모듈의 집합을 의미하며 모듈이 모여있는 디렉터리라고 생각하면 된다.

파이썬을 설치할 때 함께 설치되지 않는 모듈들은 기본적으로 패키지의 형태로
배포하고있다.

파이썬에서 기본적으로 제공하지 않더라도 외부에서 만들어진 패키지를 
이용하면 패키지에 포함된 모듈을 사용할 수 있습니다.
이런 모듈을 외부 모듈이라고 합니다.
'''

'''
2. 패키지 관리자
외부 모듈을 사용하기 위해서는 우선 모듈이 포함된 패키지를 추가로 설치해야합니다.
패키지의 추가나 삭제와 같은 작업을 수행하기 위해서는 pip라고 불리는 패키지 관리자를
사용해야합니다.


* 파이썬 3.4 이후 버전은 파이썬을 설치할 때도 pip도 함께 설치됨.
'''

'''
3. 패키지 설치
패키지 설치는 pip install 명령을 사용합니다.
기본적인 명령 형식은 다음과 같습니다.

pip install package

- numpy 패키지 설치해보기
-> numpy 패키지는 수치해석과 통계에서 많이 사용됨.
-> 넘파이 라고 읽음.
'''
import numpy as np

print(np.sum([1, 2, 3, 4, 5]))

orgin_list = [1, 3, 5, 7, 11]
result_list = []

for i in range(len(orgin_list)):
    result_list.append(orgin_list[i] + 1)
print(result_list)

orgin_list = np.array([1, 3, 5, 7, 11])
result_list = orgin_list + 1

print(list(result_list))

'''
4. 패키지 삭제 
패키지 삭제는 pip uninstall 명령을 이용합니다.
기본적인 명령 형식은 다음과 같습니다.

pip uninstall package
'''


