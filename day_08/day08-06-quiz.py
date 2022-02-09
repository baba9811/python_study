"""
파일 : day08-06-quiz
개요 : 응용 문제
page : 199 ~ 201
"""
'''
책 문제 1) 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지
모든 경우의 수를 출력하도록 구현하세요.

- 함수 정의
반환값 : 없음
함수 이름 : vending_machine()
매개변수 : 정수 money

코드 구성
def vending_machine(money):
    # 함수 구현

vending_machine(3000)

출력:
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''

def vending_machine(money):
    count = money // 700 # 몇번 뽑을 수 있는지
    for i in range(count + 1): # 처음 동작할때 0개에 잔돈 xxx원 나와야기 때문에 1번더
        print(f'음료수 = {i}개, 잔돈 = {money}')
        money -= 700

vending_machine(3000)

'''
책 문제2 ) 키(key)가 '과목명', 값(value)이 '점수'인 marks 딕셔너리를 전달하면
해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average() 함수를 구현하세요.

함수 정의
- 반환값 : 평균
- 함수 명 : get_average()
- 매개변수 : 딕셔너리 marks

코드 구성
def get_average(marks):
    # 함수 구현

marks = {'국어': 90, '영어':80, '수학': 85}
average = get_average(marks)
print('평균은 {average}점 입니다')
'''

def get_average(marks):
    total = 0

    for key in marks:
        total += marks[key]
        
    # 평균은 총점 / 과목수
    return total/len(marks)

marks = {'국어': 90, '영어':80, '수학': 85}
average = get_average(marks)
print(f'평균은 {average}점 입니다.')

'''
책 문제 3) 결혼식에 참석하는 대부분의 사람은 축의금을 냅니다.
축의금을 내는 사람의 이름과 그 사람이 낸 축의금을 딕셔너리에 저장하고 
전체 축의금의 합계를 구할 수 있는 gift() 함수를 구현하세요.

함수 정의
- 반환값 : 없음
- 함수 이름 : gift()
- 매개변수 : 딕셔너리 dic, 사람 who, 축의금 money

코드 구성
total = 0
def gift(dic, who, money):
    # 함수 구현
    
wedding = {}

gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)

print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')

출력 :
축의금 명단 : {'영희':5, '철수':3, '이모': 10}
전체 축의금 : 18
'''
total = 0
wedding = {}
def gift(who, money):
    global total
    global wedding
    wedding[who] = money
    total += money

gift('영희', 5)
gift('철수', 3)
gift('이모', 10)

print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')








