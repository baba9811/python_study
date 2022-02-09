"""
파일 : day07-05-method_quiz
개요 : 메소드 퀴즈
page : 180 ~ 181
"""

'''
예제 ) basket이라는 10가지의 과일이 들어가있는 리스트 변수가 있습니다.
pop 메소드를 이용해서 과일을 하나씩 꺼내고 basket 변수를 비워보세요.

basket = ['사과', '바나나', '사과', '체리', '망고', '망고', '망고',
'사과', '수박', '메론' ]

출력
메론
수박
사과
망고
망고
망고
체리
사과
바나나
사과
[]
'''

basket = ['사과', '바나나', '사과', '체리', '망고', '망고', '망고',
'사과', '수박', '메론']

# basket_len = int(len(basket)) # 10
# for i in range(basket_len):
#     print(basket.pop())
# print(basket)

# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket.pop())
# print(basket)

'''
1. 우리나라의 전화번호는 지역번호-국번-가입자개별번호 형식으로 되어 있습니다.
여기서 어떤 형식의 전화번를 입력하더라도 '국번'을 추출하여 출력하는 프로그램을 
구현하세요.

출력:
전화번호를 입력하세요 >>> 02-1234-5678
1234

index, split
'''
# address = input('전화번호를 입력하세요 >>>')
# first_hyphen = address.index('-') + 1
# two_hyphen = address.index('-', first_hyphen)
# print(f'{address[first_hyphen:two_hyphen]}')

# split 이용
# splits = address.split('-')
# print(f'{splits[1]}')

'''
2. 숫자3자리-숫자2자리-숫자5자리 형식(예: 123-45-67890)의 사업자등록번호를 
입력받아서 형식이 맞는지 점검하는 프로그램을 구현하세요.
단 다음 지시사항을 모두 점검해야합니다.

* 지시사항
- 전체 글자 수를 점검합니다.
- 모든 하이픈(-)의 위치가 올바른지 점검합니다.
- 하이픈(-)을 제외하면 모두 숫자인지 점검합니다.
출력 :
* 올바르지 않을때
사업자등록번호를 입력하세요(예: 123-45-67890) >> 123-사오-67890
올바른 형식이 아닙니다.
* 올바른 입력일때
사업자등록번호를 입력하세요(예: 123-45-67890) >> 123-45-67890
올바른 형식입니다.
# split, len, isdecimal, input, print
'''

#company_number = input('사업자등록번호를 입력하세요(예:123-45-67890) >>>')

company_number = '123-45-67890'
if not len(company_number) == 12:
    print('하이픈을 포함 글자수는 12자리로 맞춰주세요.')
else:
    splits = company_number.split('-')
    first = splits[0]
    two = splits[1]
    three = splits[2]

    # 3 - 2 - 5
    if len(first) == 3 and len(two) == 2 and len(three) == 5:
        if first.isdecimal() and two.isdecimal() and three.isdecimal():
            print('올바른 형식입니다.')
        else:
            print('숫자 형식에 맞게 입력해주세요.')
    else:
        print('하이픈의 위치가 알맞지 않습니다.')

'''
3. 우리 학교 성적 관리 프로그램은 다음과 같이 쉼표(',')로 구분된
문자열 형식으로 학생 이름과 성적이 입력됩니다.
이 데이터를 각각 name과 score 변수에 저장하는 프로그램을 구현하세요.

값 예시
data = '"김철수",85'
-실행->
이름은 김철수이고, 점수는 85점 입니다.
'''

data = '"김철수",85'
if data.find(',') == -1:
    print('콤마를 입력해주세요')
else:
    splits = data.split(',')
    name = splits[0].strip('\"')
    score = splits[1]
    print(f'이름은 {name}이고, 점수는 {score}입니다.')

