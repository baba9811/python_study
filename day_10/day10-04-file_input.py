"""
파일명 : day10-04-file_input
개요 : 파일 입력
page : 233 ~ 237
"""

'''
1. 텍스트 파일 읽기
파일을 읽을 때 사용하는 여러 메소드를 이용해서
hello.py 파일을 읽은 뒤 화면에 그대로 출력하는 프로그램을 구현.

* 저희가 만든 hello.py 파일 안에는 다음과 같은 텍스트가 있다.
안녕하세요
반갑습니다.
Hello.
Nice to meet you.
'''

'''
1-1 read() 메소드
read() 메소드는 파일로부터 데이터를 읽어 들이는 메소드이며
텍스트 모드와 바이너리 모드에서 다른 방식으로 동작합니다.

[ 기본 사용 형식 ]
file.read(size)

* size 인수 생략하고 사용하면 파일 전체를 읽어들임.
    = size 인수가 음수여도 동일하게 전체를 읽음.
    => size 값을 양수로 전달시 바이트 수로 인식
    
* size 인수는 바이트임
    ㄴ 1글자 != 1바이트 
        - 영문은 1글자 = 1바이트
        - 한글은 1글자 = 2바이트 or 3바이트 (인코딩에 따라 변경 )
        - UTF-8 많이 이용 ( 인코딩 )
'''

# file = open('hello.py', 'rt')
# str = file.read()
# print(str, end='')
# file.close()

'''
read() 메소드를 통해서 전체를 읽으면 그 만큼의 메모리 공간이 필요하기 때문에.
읽어야할 파일이 크다면 일부만 읽어 들이는 작업을 반복문을 이용해서 
파일 전체를 읽도록 구현하는 것이 좋습니다.
'''

# file2 = open('hello.py', mode='rt')
#
# while True:
#     read_str = file2.read(5)
#     if not read_str:
#         break
#     print(read_str, end='')
#
# file2.close()

'''
1.2. readline() 메소드
readline 메소드는 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드입니다.

만약 파일이 종료되어 더 이상 읽을 게 없으면 빈 문자열 ''을 읽어들입니다.

반복문을 이용해서 여러 번 읽어 들여야 파일 전체를 읽을 수 있습니다.
'''

# file = open('hello.py', 'rt')
#
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     print(line + '\n\n', end='')
#
# file.close()

'''
1-3. readlines() 메소드
readline은 한 줄씩 읽어서 값을 봔환해주지만.
readlines는 한 줄이 아닌 여러줄을 모두 읽어
각 라인 단위로 리스트에 저장 후 반환하는 메소드입니다. 
'''
#
# file = open('hello.py', 'rt')
# line_list = file.readlines()
# print(line_list)

'''
리스트로 반환이되는 변수는 for문 이용하는게 좋다.
'''

# file = open('hello.py', 'rt')
# line_list = file.readlines()
# for line in line_list:
#     print(line, end='')
# file.close()

'''
enumerate() 함수를 이용하면 간단하게
라인 번호도 함께 출력할 수 있습니다.
'''
#
# file = open('hello.py', 'rt')
# line_list = file.readlines()
#
# for index, line in enumerate(line_list):
#     print(f'{index + 1} {line}')
#
# file.close()

'''
sys 모듈을 이용하면 보다 쉽게 hello.py

sys 모듈에는 다음과 같은 객체가 있습니다.
- stdin 
    ㄴ 입력을 위한 객체
- stdout
    ㄴ 출력을 위한 객체이며 화면 출력 메소드인 write와 
        writelines 메소드를 사용할 수 있습니다.
    ㄴ writelines 메소드를 사용하면 리스트와 같은 반복 가능한 
        객체의 각 요소를 한 줄씩 자동 출력합니다.
'''
# import sys
#
# file = open('hello.py', 'rt')
#
# lien_list = file.readlines()
# sys.stdout.writelines(line_list)
#
# file.close()

'''
책 예제) 동요 '엄마돼지 아기돼지'의 가사가 저장되어있는 
'엄마돼지아기돼지.txt' 파일이 저장되어있습니다.
이 파일에서 '꿀'이라는 글자가 몇번 나오는지 찾는 프로그램을 만들어보세요.

[ 출력 ]
꿀은 60번 나타납니다.

[ 가사 ]
토실토실 아기돼지 젖달라고 꿀꿀꿀
엄마돼지 오냐오냐 알았다고 꿀꿀꿀
꿀꿀 꿀꿀 꿀꿀 꿀꿀
꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀
아기돼지 바깥으로 나가자고 꿀꿀꿀

토실토실 아기돼지 젖달라고 꿀꿀꿀
엄마돼지 오냐오냐 알았다고 꿀꿀꿀
꿀꿀 꿀꿀 꿀꿀 꿀꿀
꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀
아기돼지 바깥으로 나가자고 꿀꿀꿀
'''
file = open('엄마돼지아기돼지.txt', 'rt', encoding='utf-8')

lien_list = file.readlines()

count = 0

for line in lien_list:
    count += line.count('꿀')
    # for ch in line:
    #     if ch == '꿀':
    #         count += 1

print(f'꿀은 전체 {count}번 나타납니다.')
file.close()

