from math import *
from random import *
from time import *
from datetime import *
"""
파일명 : day09-02-standard_module
개요 : 표준 모듈
page : 210 ~ 218
"""

'''
표준 모듈이란 파이썬에 기본적으로 설치되어 있는 모듈을 의미합니다.
표준 모듈들은 별로도 설치하지 않고 import 후 바로 사용 가능합니다.

- python 내부에 모듈들이 이미 만들어져있는게 있다!!!!! 
우리는 이를 이용할 뿐!!!!!!! :)
'''

'''
1. math 모듈
- math = 수학 
수학에 관한 다양한 함수와 변수가 내장되어있습니다.
1-1. pi
1-2. ceil(), floor()
1-3. trunc()
1-4. sqrt()
1-5. pow()
'''

'''
1-1. 원주율 pi 변수 ***
원주율은 흔히 3.14로 알고있지만.
실제로는 뒤에 많은 수가 생략되어있습니다.
3.141592653589793....
이를 완전히 사용하고 싶을때 다음과 같이 사용합니다.
'''
# print(pi)

'''
1-2. ceil(), floor() 함수
두 함수는 모두 전달된 값을 정수로 올림 처리하거나
내림 처리 합니다.
ceil() - 올림처리
floor() - 내림처리
'''
# 올림처리
# print(ceil(1.1))

# 내림
# print(floor(1.9))

'''
1-3. trunc() 함수
trunc() 함수를 사용해서 전달된 값을 정수로 절사할 수 있습니다.
floor 랑 비슷한데 음수쪽에서 확실하게 달라짐.
'''

# print(trunc(-1.9))
# print(floor(-1.9))

'''
1-4. sqrt() 함수
sqrt() 함수로 제곱근을 구할 수 있습니다.
( 제곱근 = 수학의 루트 )
'''
# print(sqrt(25))

'''
1-5. pow() 함수
pow() 함수로 제곱을 구할 수 있습니다.
'''

# print(pow(2, 3)) # 실수로 반환
# # pow(2,3) == 2**3
# print(2**3) # 정수로 반환

'''
2. random 모듈
난수( random number )를 생성하는 모듈입니다. 
난수를 통해서 간단한 게임이나 확률 처리도 할 수 있습니다.
2-1. randint()
2-2. randrange()
2-3. random()
2-4. choice()
2-5. sample() 
2-6. shuffle()
'''

'''
2-1. randint()
- randint() 함수는 전달하는 두 인수 사이의 정수를 임의로 생성합니다.
1에서 10이하의 범위에서 정수 하나를 임의로 생성하려면
randint(1, 10) 과 같이 작성하면됩니다.
'''
print(randint(1, 10))

'''
2-2. randrange()
randrange() 함수는 range() 함수와 사용 방법이 비슷
range() 함수는 특정 범위의 정숫값들을 모두 생성할 수 있지만.
randrange() 함수는 그 특정 범위에 속한 정수 중에서 하나만 임의로 생성

- randint와 randrange와 차이는 end가 미만이냐, 이하이냐 차이
* randint는 이하.
  randrange는 미만.
'''

# 0 ~ 9 범위 한개의 수 반환
print(randrange(10))
# 1 ~ 9 범위 한 개의 수 반환
print(randrange(1, 10))
# 1 ~ 9 / jump 2 범위 한 개의 수 반환
print(randrange(1, 10, 2))

'''
2-3. random() 함수
random() 함수는 0이상 1미만 범위에서 임의의 실수를 생성합니다.
0이상 1미만 범위를 백분율로 환산하면 0% 이상 100% 미만이기 때문에 확률을 처리할 때 사용
'''
print(random())
print(f'{int(random() * 100)}%')

# ex ) 50%의 확률로 성공하는 코인 게임을 만들어보자.
# 성공하면 성공!!!!! 실패하면 실패...를 띄워보세요.

if random() < 0.5:
    print('성공 !!!!')
else:
    print('실패....')

'''
2-4. choice() 함수
choice() 함수는 전달된 시퀀스 자료형에 속한 요소 중에서 
하나를 임의로 반환합니다.
'''
seasons = ['봄', '여름', '가을', '겨울']
print(choice(seasons))

'''
문제 ) 계절별로 다음과 같이 출력해보세요.

봄 - 꽃보로 가죠~
여름 - 바다로 가죠~
가을 - 단풍보로 가죠~~
겨울 - 스키장 가죠~~
'''
seasons = ['봄', '여름', '가을', '겨울']
season = choice(seasons)
if season == '봄':
    print("꽃보로 가죠~~")
elif season == '여름':
    print("바다로 가죠~~~")
elif season == '가을':
    print('단풍보로 가죠~~~')
else:
    print('스키장 가죠~~~')

'''
2-5. sample() 함수
sample() 함수는 전달된 시퀀스 자료형에 속한 요소 중 지정된 개수의
요소를 임의로 반환합니다.
반환 결과는 '리스트 자료형'이며 '중복 없이' 임의의 요소가 선택됩니다.
'''

# 간단한 로또 번호 생성 코드를 만들어보자.
# 1부터 45까지 정수를 생성한 뒤 6개의 요소를 임의로 추출해보자.
# -- 중복 없이 6개의 요소가 추출됨.
print(sample(range(1, 46), 6))

'''
2-6. shuffle() 함수
shuffle() 함수는 말 그대로 임의로 섞는 것을 의미합니다.
전달된 시퀀스 자료형에 속한 요소의 순서를 임의로 조정하여 다시 배치하는
함수
** 실제 전달된 시퀀스 자료형의 순서가 재배치됨.
'''
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)

'''
책 기본 예제 ) 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 
맞히는 프로그램입니다.

사용자가 맞힐 때까지 게임은 계속됩니다.

출력 : 
주사위 값은 얼마일까요? >>>1
오답입니다. 다시 시도하세요.
주사위 값은 얼마일까요? >>>2
오답입니다. 다시 시도하세요.
주사위 값은 얼마일까요? >>>3
3! 정답입니다.
'''

# dice = randint(1, 6)
# while True:
#     user = int(input('주사위 값은 얼마일까요? >>>'))
#     if dice == user:
#         print(f'{dice}! 정답입니다.')
#         break
#     else:
#         print('오답입니다. 다시 시도하세요')

'''
3. time 모듈
시간 처리에 관련된 time 모듈은 다음과 같은 함수를 제공합니다.
3-1. time()
3-2. ctime()
3-3. strftime()
3-4. sleep()
'''

'''
3-1. time() 함수
1970년 1월 1일 0시 0분 0초부터 현재까지 경과된 시간(timestamp)을 반환합니다.
소수점 이하는 마이크로초를 의미합니다.
time() 함수는 현재 시간을 반환하므로 실행 시점에 따라 결과가 다르게 나타납니다.
'''
# print(time())

'''
3-2. ctime() 함수
인수로 전달된 시간(timestamp)을 형식에 갖춰 반환
'''
# print(ctime(time()))

'''
3-3. strftime() 함수
인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘 날짜 데이터가 문자열로
반환됩니다.
strftime() 함수에서 사용할 수 있는 중요한 지시자는 다음과 같습니다.
** 대소문자 중요!!!!
연도 - %Y
월 - %m
일 - %d
시 - %H
분 - %M
초 - %S 
'''
# 2021-07-24 17:xx:xx
print(strftime('%Y-%m-%d %H:%M:%S'))

'''
3-4. sleep() 함수
인수로 전달된 초(second) 만큼 시스템을 일시 중지시킵니다.
'''
# sleep(randint(1, 3))
# print('아아아')

'''
4. datetime 모듈
datetime 모듈은 날짜와 시간 데이터를 처리할 때 사용합니다.
datetime 내장 모듈은 다음과 같은 메소드, 함수, 변수들을 제공합니다.
1. datetime.now() 
2. date() 
3. time()
4. year, month, day, hour, minute, second
5. timedelta()
6. datetime.total_seconds()
'''

'''
1. datetime.now() 메소드
* 함수가 아닌 메소드입니다.
now() 메소드는 datetime 클래스 내부에 정의되어있는 메소드입니다.
시스템의 현재 날짜와 시간을 반환합니다.
'''

present = datetime.now()
print(present)

# datetime.datetime.now()
# => 모듈.클래스.메소드

'''
4-2. date() 함수
date() 함수는 특정 '날짜'를 만들어서 반환합니다.
'''

my_date = date(year=2021, month=7, day=20)
print(my_date)

'''
4-3. time() 함수
time() 함수는 특정 '시간'을 만들어서 반환합니다.
'''
wake = time(10, 48, 0)
print(wake)

'''
4-4. 날짜 / 시간 관련 필드값
특정 날짜에서 원하는 데이터만 추출하고자 하는 경우에는 해당 필드값을 이용합니다.
'''

today = datetime.now()
print(f'{today.year} 연도')
print(f'{today.month} 월')
print(f'{today.day} 일')
print(f'{today.hour} 시간')
print(f'{today.minute} 분')
print(f'{today.second} 초')

'''
4-5. timedelta() 함수
timedelta() 함수는 날짜 / 시간 데이터의 연산을 위하여 사용하고
주요 사용 방법은 다음과 같습니다.

1주 : timedelta(weeks=1)
1일 : timedelta(days=1)
1시간 : timedelta(hours=1)
1분 : timedelta(minutes=1)
1초 : timedelta(seconds=1)
'''

# now() 메소드와 timedelta() 함수를 이용해서 어제, 오늘, 내일을 만들어보자.
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(tomorrow)

# 문제 ) 일주일 전, 일주일 후를 출력해보세요.
week_one_before = today - timedelta(weeks=1)
week_one_after = today + timedelta(weeks=1)
print(week_one_before)
print(week_one_after)

'''
4-6 datetime.total_seconds() 메소드
- 함수가 아닌 메소드입니다.
total_seconds() 메소드는 어떤 기간에 포함된 총 시간을 초(seconds)로 반환합니다.
timedelta.total_seconds() 형식으로 사용합니다.
'''

date1 = date(2020, 8, 25)
date2 = date(2020, 8, 26)
print(date2 - date1)
print(type(date2 - date1))
print((date2 - date1).total_seconds())

'''
책 예제 ) 다음은 1부터 10,000,000(천만) 까지의 합계를 구하고 
그 결과와 연산에 걸린 시간을 함께 출력하는 프로그램입니다.

출력:
총 합은 ****입니다.
총 ***초가 소요됬습니다.
'''

start = datetime.now()
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()

print(f'총 합은 {total} 입니다.')
print(f'총 {elapse} 초가 소용됬습니다.')















