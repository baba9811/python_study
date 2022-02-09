"""
파일명 : anser
"""
'''
개인정보의 보안 처리를 위하여 주어진 인수의 일부를 *로 바꿔서 
반환하는 함수를 만들어서 이를 모듈러 저장하는 프로그램입니다.

다음과 같은 조건으로 모듈을 만들어서 사용해보세요.

[ 모듈 생성하기 ]
모듈명 : my_secure.py
- 함수
secure_name() 함수 : 김철수 -> 김**
secure_no() 함수 : 951012-1234567 -> 951012-1******
secure_phone() 함수 : 010-1234-5678 -> 010-****-5678

[ 모듈 사용하기 ]
현재 anser 파일에서 my_secure 모듈을 사용해서 
다음과 같은 출력을 해보자.

[ 출력 결과 ]
김**
951012-1******
010-****-5678
'''
import my_secure

print(my_secure.secure_name('김철수'))
print(my_secure.secure_no('951012-1234567'))
print(my_secure.secure_phone('010-1234-5678'))









