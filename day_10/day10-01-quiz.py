import random
import time
import math
"""
파일명 : day10-01-quiz
- 응용문제
- 221 ~ 222
"""

'''
1. 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

[ 지시사항 ]
- 1에서 45사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
- 다음 과정을 6번 반복합니다.
    - pot 리스트를 무작위로 섞어줍니다.
    - pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
    - 2초 동안 잠시 멈춥니다.
- jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
- jackpot 리스트의 모든 요소를 출력합니다.

[ 출력 ]
1번째 당첨번호는 38입니다.
2번째 당첨번호는 42입니다.
3번째 당첨번호는 25입니다.
4번째 당첨번호는 32입니다.
5번째 당첨번호는 40입니다.
6번째 당첨번호는 7입니다.
이번 당첨번호는 [38, 42, 25, 32, 40, 7 ]
'''
#
# # '1에서 45사이의 모든 정수'를 '순서'대로 pot '리스트'에 '저장'합니다.
# pot = list(range(1, 46))
#
# # pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
# jackpot = []
#
# # 다음 과정을 6번 반복합니다.
# for i in range(1, 7):
#     # pot 리스트를 무작위로 섞어줍니다.
#     random.shuffle(pot)
#     # pot 리스트의 마지막 숫자를 하나만 '빼서'
#     num = pot.pop()
#     print(f'{i}번째 당첨번호는 {num}입니다')
#     jackpot.append(num)
#     # 2초 동안 잠시 멈춥니다.
#     time.sleep(2)
#
# # jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
# jackpot.sort()
# print(f'이번 당첨번호는 {jackpot}')

'''
예제 ) 다음 지시사항에 따라 UpDown게임을 구현하세요.

[ 지시사항 ]
- 1에서 100사이의 정수중 하나를 임의로 생성하면 사용자는 그 숫자를
맞힐 때까지 값을 예상하여 입력합니다.
- 사용자가 입력한 값이 정답보다 작으면 Up, 정답보다 크면 Down을 출력합니다.
- 정답을 맞히면 몇 초만에 정답을 맞혔는지 출력하세요,
이때 소수 아래 값은 내림 처리하여 정수로 출력하세요.

[ 출력 ]
UpDown 게임을 시작합니다.
어떤 값일까요? >>>50
Down
어떤 값일까요? >>>25
Up
어떤 값일까요? >>>35
Down
어떤 값일까요? >>>27
정답입니다~!
18초 만에 성공했습니다.
'''
#
# print('UpDown 게임을 시작합니다.')
# # 1에서 100사이의 정수중 하나를 임의로 생성
# num = random.randint(1, 100)
#
# # 정답을 맞히면 몇 초만에 정답을 맞혔는지 출력하세요
# start = time()
#
# # 사용자는 그 숫자를 맞힐 때까지 값을 예상하여 입력합니다.
# while True:
#     input_num = int(input('어떤 값일까요? >>>'))
#     if num == input_num:
#         print('정답입니다.')
#         end = time()
#         # 소수 아래 값은 내림 처리 하여 정수로 출력하세요
#         print(f'{math.floor(end - start)} 초 걸렸습니다.')
#         break
#     elif input_num < num:
#         # 사용자가 입력한 값이 정답보다 작으면 Up
#         print('Up')
#     elif input_num > num:
#         # 정답보다 크면 Down을 출력합니다.
#         print('Down')

'''
예제) 다음 지시사항에 따라 문제를 만들어보세요.

[ 지시사항 ]
- 롱소드, 숏소드 두개의 무기가 담긴 dict 타입의 변수를 선언하세요.
- 다음 조건이 만족되면 반복문을 종료하세요.
    - 사용자가 강화를 원하지 않는다.
    - 더이상 강화할 수 있는 무기가 없다.
- 강화를 시작하면 1~3초 사이의 시간으로 잠시 일시 정지 시키세요.
- 50% 확률로 강화가 성공 / 실패 하게 하세요.
- 성공과 실패시 다음과같은 작업을 해주세요.
    - 성공
        ㄴ 현재 선택된 무기의 강화 수치를 +1 해주세요.
    - 실패
        ㄴ 강화 실패.. 띄워주고 해당 무기를 dict 변수에서 없애주세요.    
'''

weapon = {
    '롱소드': 0,
    '숏소드': 0
}

while True:
    if len(weapon) > 0:
        choice_weapon = input(f'강화하고 싶은 무기를 선택하세요. '
                              f'{list(weapon.keys())} >>>')
        if choice_weapon in weapon:
            is_reinforce = input(f'{choice_weapon} '
                                 f'({weapon[choice_weapon]}) 무기를 선택하셨습니다.'
                                 f'강화하시겠습니까? (Y/N) >>')
            if is_reinforce.upper() == 'Y':
                print('강화를 시작합니다!!!!.....')
                time.sleep(random.randint(1, 3))
                if random.random() < 0.5:
                    print('강화 성공!!!!!!')
                    weapon[choice_weapon] += 1
                else:
                    print('강화 실패.....')
                    del weapon[choice_weapon]
            elif is_reinforce.upper() == 'N':
                print('강화를 종료합니다.')
                break
            else:
                print('다시 입력해주세요.')
                continue

    else:
        print('강화할 수 있는 무기가 없습니다.')
        break


