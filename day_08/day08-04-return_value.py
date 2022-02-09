"""
파일 : day08-04-return_value
개요 : 반환값
page : 192 ~ 196
"""
'''
함수 호출 결과를 반환값(return value)이라고 합니다.
반환값이 있으면 함수 내부에서 return문을 통해 값을 반환 할 수 있고
반환값이 없으면 함수 내부에 return문을 작성할 필요가 없습니다.
'''

'''
1. 반환값이 있는 함수
address() 함수를 호출하면 본문에 작성된 주소가 결과로 반환되게 해보자 
'''

def address(): # 2
    add = '우편번호 12345\n' # 3
    add += '서울시 영등포구 여의도동' # 4
    return add # 5

print(address()) # 1 - address() 6 - print()

'''
2. 다중 반환
파이썬은 하나의 반환값도 처리할 수 있고,
여러 개의 반환값도 처리할 수 있습니다.
'''

def calculator(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

a, b, c, d = calculator(1, 2, 3, 4, 5)
print('합계', a)
print('평균', b)
print('최댓값', c)
print('최솟값', d)

print(type(calculator(1, 2, 3, 4, 5)))
print(calculator(1, 2, 3, 4, 5))

result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])
print('평균', result[1])
print('최댓값', result[2])
print('최솟값', result[3])

'''
3. 함수의 종료를 위한 return
반환 값이 있으면 return문을 사용해 반환하고,
반환값이 없으면 return문을 생략하면 된다.
하지만 반환 값이 없을때고 return 을 작성할 때가 있다.
-> 함수를 종료하고 싶을때 return 을 작성한다.
'''

def a():
    while True:
        print('a')
        while True:
            print('b')
            return # 이 함수는 여기서 종료!!!
a()

def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
        return
    print('에너지가 충전되었습니다.')

charge(1)
charge(-1)

'''
예제 ) 1~ 100까지의 숫자를 출력하는데 
현재 출력되는 숫자가 68일때 정지가 되는 함수를 만들어보세요.
함수명 : number_count()
1
2
3
...
68
'''

def number_count():
    for i in range(1, 100):
        if i == 68:
            print(i)
            return
        else:
            print(i)

number_count()

'''
책 예제 ) 커피 자판기 프로그램입니다. 
커피 자판기는 다음과 같이 동작합니다.

1. 커피 자판기에 돈과 주문할 커피를 전달합니다.
2. 주문할 수 있는 커피의 종류와 가격은 다음과 같습니다.
    {
        "아메리카노": 1000,
        "카페라떼": 1500,
        "카푸치노": 2000
    }
3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환합니다.
4. 구매 금액이 부족하면 입력한 돈을 그대로 반환합니다.
5. 정상 주문이면 주문한 커피와 잔돈을 반환합니다.

출력:
- 없는 커피를 주문한 경우
커피를 선택하세요(아메리카노, 카페라떼, 카푸치노) >>> 마키아또
얼마를 내시나요? >>> 15000
15000원에 마키아또를 선택하셨습니다.
마키아또는 판매하지 않습니다.
잔돈 15000원, 커피 없는 메뉴
- 주문 금액이 부족한 경우
커피를 선택하세요(아메리카노, 카페라떼, 카푸치노) >>> 아메리카노
얼마를 내시나요? >>> 500
500원에 아메리카노를 선택하셨습니다.
아메리카노는 1000원입니다.
잔돈 500원, 커피 금액 부족 
- 정상 주문
커피를 선택하세요(아메리카노, 카페라떼, 카푸치노) >>> 아메리카노
얼마를 내시나요? >>> 2000
2000원에 아메리카노를 선택하셨습니다.
잔돈 1000원, 커피 아메리카노 
'''

# 1. 커피 자판기에 돈과 주문할 커피를 전달합니다.
order = input('커피를 선택하세요(아메리카노, 카페라떼, 카푸치노) >>>')
money = int(input('얼마를 내시나요? >>>'))

def coffee_machine(money, pick):
    print(f'{money}원에 {pick}를 선택하셨습니다.')

    menu = {
        "아메리카노": 1000,
        "카페라떼": 1500,
        "카푸치노": 2000
    }
    # 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환합니다.
    if pick not in menu:
        print(f'{pick}는 판매하지 않습니다.')
        return money, '없는 메뉴'

    # 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환합니다.
    elif menu[pick] > money:
        print(f'{pick}는 {menu[pick]}원 입니다.')
        return money, '금액 부족'
    else:
        return money - menu[pick], pick

change, coffee = coffee_machine(money, order)
print(f'잔돈 {change}원, 커피 {coffee}')








